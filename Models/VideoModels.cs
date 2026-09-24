namespace Ben10Videos.Models;

public class Universe
{
    public string Id { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Tagline { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string ReleaseYears { get; set; } = string.Empty;
    public string AccentColor { get; set; } = "#00ff41";
    public string PosterClass { get; set; } = string.Empty;
    public string BannerImage { get; set; } = string.Empty;
    public List<Season> Seasons { get; set; } = new();
}

public class Season
{
    public int SeasonNumber { get; set; }
    public string Title { get; set; } = string.Empty;
    public string ReleaseYear { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public List<Episode> Episodes { get; set; } = new();
}

public class Episode
{
    public string Id { get; set; } = string.Empty;
    public string UniverseId { get; set; } = string.Empty;
    public int SeasonNumber { get; set; }
    public int EpisodeNumber { get; set; }
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string Duration { get; set; } = "22 min";
    public string AirDate { get; set; } = string.Empty;
    public string FeaturedAliens { get; set; } = string.Empty;
    public string TeraBoxUrl { get; set; } = string.Empty;
    public string ImageUrl { get; set; } = string.Empty;
}

public class WatchViewModel
{
    public List<Universe> AllUniverses { get; set; } = new();
    public Universe CurrentUniverse { get; set; } = new();
    public Season CurrentSeason { get; set; } = new();
    public List<Episode> DisplayEpisodes { get; set; } = new();
    public string? SearchQuery { get; set; }
    public int TotalEpisodesInUniverse { get; set; }
}

public class UpdateLinkRequest
{
    public string EpisodeId { get; set; } = string.Empty;
    public string TeraBoxUrl { get; set; } = string.Empty;
}
