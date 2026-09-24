using System.Text.Json;
using Ben10Videos.Models;

namespace Ben10Videos.Services;

public class VideoRepository : IVideoRepository
{
    private readonly string _filePath;
    private readonly IWebHostEnvironment _env;
    private readonly ILogger<VideoRepository> _logger;
    private static readonly object _lock = new();
    private List<Universe> _universes = new();

    public VideoRepository(IWebHostEnvironment env, ILogger<VideoRepository> logger)
    {
        _env = env;
        _logger = logger;
        _filePath = Path.Combine(_env.ContentRootPath, "Data", "episodes.json");
        LoadData();
    }

    private void LoadData()
    {
        lock (_lock)
        {
            try
            {
                if (File.Exists(_filePath))
                {
                    var json = File.ReadAllText(_filePath);
                    var options = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
                    _universes = JsonSerializer.Deserialize<List<Universe>>(json, options) ?? new();
                    _logger.LogInformation("Loaded {Count} universes from {Path}", _universes.Count, _filePath);
                }
                else
                {
                    _logger.LogWarning("episodes.json not found at {Path}", _filePath);
                    _universes = new();
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to load episodes.json");
                _universes = new();
            }
        }
    }

    public List<Universe> GetAllUniverses()
    {
        lock (_lock)
        {
            return _universes;
        }
    }

    public Universe? GetUniverseById(string universeId)
    {
        lock (_lock)
        {
            return _universes.FirstOrDefault(u => 
                string.Equals(u.Id, universeId, StringComparison.OrdinalIgnoreCase));
        }
    }

    public Season? GetSeason(string universeId, int seasonNumber)
    {
        var universe = GetUniverseById(universeId);
        return universe?.Seasons.FirstOrDefault(s => s.SeasonNumber == seasonNumber);
    }

    public List<Episode> GetEpisodes(string universeId, int seasonNumber)
    {
        var season = GetSeason(universeId, seasonNumber);
        return season?.Episodes ?? new();
    }

    public Episode? GetEpisodeById(string episodeId)
    {
        lock (_lock)
        {
            foreach (var u in _universes)
            {
                foreach (var s in u.Seasons)
                {
                    var ep = s.Episodes.FirstOrDefault(e => 
                        string.Equals(e.Id, episodeId, StringComparison.OrdinalIgnoreCase));
                    if (ep != null) return ep;
                }
            }
            return null;
        }
    }

    public List<Episode> SearchEpisodes(string query, string? universeId = null)
    {
        if (string.IsNullOrWhiteSpace(query))
        {
            return new();
        }

        var normalized = query.Trim().ToLowerInvariant();
        var results = new List<Episode>();

        lock (_lock)
        {
            var searchScope = string.IsNullOrEmpty(universeId)
                ? _universes
                : _universes.Where(u => string.Equals(u.Id, universeId, StringComparison.OrdinalIgnoreCase));

            foreach (var u in searchScope)
            {
                foreach (var s in u.Seasons)
                {
                    foreach (var ep in s.Episodes)
                    {
                        if (ep.Title.ToLowerInvariant().Contains(normalized) ||
                            ep.Description.ToLowerInvariant().Contains(normalized) ||
                            ep.FeaturedAliens.ToLowerInvariant().Contains(normalized) ||
                            $"episode {ep.EpisodeNumber}".Contains(normalized) ||
                            $"ep {ep.EpisodeNumber}".Contains(normalized) ||
                            $"s{ep.SeasonNumber:D2}e{ep.EpisodeNumber:D2}".ToLowerInvariant().Contains(normalized))
                        {
                            results.Add(ep);
                        }
                    }
                }
            }
        }

        return results;
    }

    public bool UpdateTeraBoxUrl(string episodeId, string newUrl)
    {
        lock (_lock)
        {
            var ep = GetEpisodeById(episodeId);
            if (ep == null) return false;

            ep.TeraBoxUrl = newUrl.Trim();

            try
            {
                var options = new JsonSerializerOptions { WriteIndented = true };
                var json = JsonSerializer.Serialize(_universes, options);
                File.WriteAllText(_filePath, json);
                _logger.LogInformation("Updated TeraBox URL for episode {Id}", episodeId);
                return true;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to persist updated TeraBox URL for {Id}", episodeId);
                return false;
            }
        }
    }
}
