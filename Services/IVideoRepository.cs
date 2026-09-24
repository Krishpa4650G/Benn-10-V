using Ben10Videos.Models;

namespace Ben10Videos.Services;

public interface IVideoRepository
{
    List<Universe> GetAllUniverses();
    Universe? GetUniverseById(string universeId);
    Season? GetSeason(string universeId, int seasonNumber);
    List<Episode> GetEpisodes(string universeId, int seasonNumber);
    Episode? GetEpisodeById(string episodeId);
    List<Episode> SearchEpisodes(string query, string? universeId = null);
    bool UpdateTeraBoxUrl(string episodeId, string newUrl);
}
