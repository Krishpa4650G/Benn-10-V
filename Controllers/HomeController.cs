using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Ben10Videos.Models;
using Ben10Videos.Services;

namespace Ben10Videos.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly IVideoRepository _repo;

    public HomeController(ILogger<HomeController> logger, IVideoRepository repo)
    {
        _logger = logger;
        _repo = repo;
    }

    public IActionResult Index()
    {
        var universes = _repo.GetAllUniverses();
        return View(universes);
    }

    public IActionResult About()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
