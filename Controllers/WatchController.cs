using Microsoft.AspNetCore.Mvc;
using Ben10Videos.Models;
using Ben10Videos.Services;

namespace Ben10Videos.Controllers;

public class WatchController : Controller
{
    private readonly IVideoRepository _repo;
    private readonly ILogger<WatchController> _logger;

    public WatchController(IVideoRepository repo, ILogger<WatchController> logger)
    {
        _repo = repo;
        _logger = logger;
    }

    // GET: /Watch or /Watch?universe=classic&season=1
    public IActionResult Index(string? universe, int? season, string? search)
    {
        var allUniverses = _repo.GetAllUniverses();
        if (!allUniverses.Any())
        {
            return View("Error", new ErrorViewModel { RequestId = "No universe data found" });
        }

        // Determine current universe (defaults to first or requested)
        var selectedUniverse = (!string.IsNullOrEmpty(universe)
            ? allUniverses.FirstOrDefault(u => string.Equals(u.Id, universe, StringComparison.OrdinalIgnoreCase))
            : null) ?? allUniverses.First();

        // Determine current season
        var selectedSeasonNumber = season.GetValueOrDefault(
            selectedUniverse.Seasons.FirstOrDefault()?.SeasonNumber ?? 1);
        
        var selectedSeason = selectedUniverse.Seasons.FirstOrDefault(s => s.SeasonNumber == selectedSeasonNumber)
            ?? selectedUniverse.Seasons.FirstOrDefault()
            ?? new Season { SeasonNumber = 1, Title = "Season 1" };

        List<Episode> displayEpisodes;
        if (!string.IsNullOrWhiteSpace(search))
        {
            displayEpisodes = _repo.SearchEpisodes(search, selectedUniverse.Id);
        }
        else
        {
            displayEpisodes = selectedSeason.Episodes;
        }

        var totalInUniverse = selectedUniverse.Seasons.Sum(s => s.Episodes.Count);

        var model = new WatchViewModel
        {
            AllUniverses = allUniverses,
            CurrentUniverse = selectedUniverse,
            CurrentSeason = selectedSeason,
            DisplayEpisodes = displayEpisodes,
            SearchQuery = search,
            TotalEpisodesInUniverse = totalInUniverse
        };

        return View(model);
    }

    // GET: /Watch/Transfer?id=classic-s01e01
    public IActionResult Transfer(string id)
    {
        if (string.IsNullOrEmpty(id))
        {
            return RedirectToAction(nameof(Index));
        }

        var episode = _repo.GetEpisodeById(id);
        if (episode == null)
        {
            return NotFound("Episode not found in Galvan Archives.");
        }

        var universe = _repo.GetUniverseById(episode.UniverseId);
        ViewBag.Universe = universe;

        return View(episode);
    }

    // GET: /Watch/Admin
    public IActionResult Admin()
    {
        var universes = _repo.GetAllUniverses();
        return View(universes);
    }

    // POST: /Watch/UpdateLink
    [HttpPost]
    public IActionResult UpdateLink([FromBody] UpdateLinkRequest req)
    {
        if (req == null || string.IsNullOrWhiteSpace(req.EpisodeId) || string.IsNullOrWhiteSpace(req.TeraBoxUrl))
        {
            return BadRequest(new { success = false, message = "Episode ID and TeraBox URL are required." });
        }

        var updated = _repo.UpdateTeraBoxUrl(req.EpisodeId, req.TeraBoxUrl);
        if (updated)
        {
            return Ok(new { success = true, message = "TeraBox link updated successfully in Galvan database!" });
        }

        return NotFound(new { success = false, message = "Episode could not be found." });
    }
}
