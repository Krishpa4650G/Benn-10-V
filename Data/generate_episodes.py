import json
import os

universes = [
    {
        "Id": "classic",
        "Name": "Ben 10 Classic",
        "Tagline": "The Original Summer Journey",
        "Description": "Ten-year-old Ben Tennyson discovers the Omnitrix, a mysterious alien watch granting him the power to transform into 10 extraordinary alien heroes.",
        "ReleaseYears": "2005 - 2008",
        "AccentColor": "#f7df1e",
        "PosterClass": "classic",
        "BannerImage": "/images/classic-banner.jpg",
        "Seasons": [
            {
                "SeasonNumber": 1,
                "Title": "Season 1",
                "ReleaseYear": "2005 - 2006",
                "Description": "Ben discovers the Omnitrix during summer vacation and battles Dr. Animo, Vilgax's drones, and the bounty hunters.",
                "Episodes": [
                    {
                        "Id": "classic-s01e01",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 1,
                        "Title": "And Then There Were 10",
                        "Description": "During a summer road trip with Grandpa Max and cousin Gwen, Ben finds an alien pod in the woods containing the mysterious Omnitrix.",
                        "Duration": "23 min",
                        "AirDate": "Dec 27, 2005",
                        "FeaturedAliens": "Heatblast, Wildmutt, Diamondhead, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e01"
                    },
                    {
                        "Id": "classic-s01e02",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 2,
                        "Title": "Washington B.C.",
                        "Description": "Dr. Aloysius Animo uses his Transmodulator device to resurrect prehistoric creatures and mutate modern animals.",
                        "Duration": "22 min",
                        "AirDate": "Jan 13, 2006",
                        "FeaturedAliens": "Four Arms, Stinkfly, Grey Matter",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e02"
                    },
                    {
                        "Id": "classic-s01e03",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 3,
                        "Title": "The Krakken",
                        "Description": "While fishing at Lake Verdan, Ben and Grandpa Max encounter a legendary giant lake monster and an obsessed poacher.",
                        "Duration": "22 min",
                        "AirDate": "Jan 14, 2006",
                        "FeaturedAliens": "Ripjaws, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e03"
                    },
                    {
                        "Id": "classic-s01e04",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 4,
                        "Title": "Permanent Retirement",
                        "Description": "The Tennysons visit Aunt Vera in a Florida retirement village, only to find the residents replaced by shape-shifting alien Limax.",
                        "Duration": "22 min",
                        "AirDate": "Jan 21, 2006",
                        "FeaturedAliens": "Ghostfreak, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e04"
                    },
                    {
                        "Id": "classic-s01e05",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 5,
                        "Title": "Hunted",
                        "Description": "Vilgax hires three lethal alien bounty hunters—Tetrax Shard, Kraab, and Sixsix—to retrieve the Omnitrix from Ben.",
                        "Duration": "22 min",
                        "AirDate": "Jan 28, 2006",
                        "FeaturedAliens": "Diamondhead, Grey Matter",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e05"
                    },
                    {
                        "Id": "classic-s01e06",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 6,
                        "Title": "Tourist Trap",
                        "Description": "In a wacky roadside tourist attraction Sparksville, Ben accidentally releases tiny electricity-devouring aliens called Megawhatts.",
                        "Duration": "22 min",
                        "AirDate": "Feb 4, 2006",
                        "FeaturedAliens": "Heatblast, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e06"
                    },
                    {
                        "Id": "classic-s01e07",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 7,
                        "Title": "Kevin 11",
                        "Description": "In New York City, Ben meets Kevin Levin, a troubled runaway mutant with the power to absorb energy and alien DNA.",
                        "Duration": "22 min",
                        "AirDate": "Feb 11, 2006",
                        "FeaturedAliens": "Four Arms, XLR8, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e07"
                    },
                    {
                        "Id": "classic-s01e08",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 8,
                        "Title": "The Alliance",
                        "Description": "A criminal named Joey bonds with Vilgax's battle drone to become the cybernetic super-villainess Rojo.",
                        "Duration": "22 min",
                        "AirDate": "Feb 18, 2006",
                        "FeaturedAliens": "Four Arms, XLR8, Upgrade",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e08"
                    },
                    {
                        "Id": "classic-s01e09",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 9,
                        "Title": "Last Laugh",
                        "Description": "Ben must confront his deep fear of clowns when the evil Zombozo and his Circus Freaks drain the happiness from townspeople.",
                        "Duration": "22 min",
                        "AirDate": "Feb 25, 2006",
                        "FeaturedAliens": "Ghostfreak, Wildmutt, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e09"
                    },
                    {
                        "Id": "classic-s01e10",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 10,
                        "Title": "Lucky Girl",
                        "Description": "Ben battles the dark sorcerer Hex. During the fight, Gwen gains Hex's mystical amulet and becomes a superhero herself.",
                        "Duration": "22 min",
                        "AirDate": "Mar 4, 2006",
                        "FeaturedAliens": "Upgrade, Ripjaws, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e10"
                    },
                    {
                        "Id": "classic-s01e11",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 11,
                        "Title": "A Small Problem",
                        "Description": "Ben gets stuck in Grey Matter's form and is captured by Howell Wayneright, a member of the alien-hunting organization The Organization.",
                        "Duration": "22 min",
                        "AirDate": "Mar 11, 2006",
                        "FeaturedAliens": "Grey Matter",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e11"
                    },
                    {
                        "Id": "classic-s01e12",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 12,
                        "Title": "Side Effects",
                        "Description": "Ben catches a cold that alters his alien forms' biology while stopping Clancy, a villain who commands swarms of insects.",
                        "Duration": "22 min",
                        "AirDate": "Mar 18, 2006",
                        "FeaturedAliens": "Heatblast (Ice), Wildmutt, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e12"
                    },
                    {
                        "Id": "classic-s01e13",
                        "UniverseId": "classic",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 13,
                        "Title": "Secrets",
                        "Description": "A fully healed Vilgax descends onto Earth to seize the Omnitrix personally. Grandpa Max reveals his true past as a Plumber.",
                        "Duration": "23 min",
                        "AirDate": "Mar 25, 2006",
                        "FeaturedAliens": "Diamondhead, XLR8, Heatblast, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s01e13"
                    }
                ]
            },
            {
                "SeasonNumber": 2,
                "Title": "Season 2",
                "ReleaseYear": "2006",
                "Description": "The Tennyson team encounters Kevin's mutated amalgamation, the Forever Knights, and the terrifying escape of Ghostfreak.",
                "Episodes": [
                    {
                        "Id": "classic-s02e01",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 1,
                        "Title": "Truth",
                        "Description": "Grandpa Max reunites with his former Plumber partner Phil, who has been secretly releasing captured aliens for cash bounties.",
                        "Duration": "22 min",
                        "AirDate": "May 29, 2006",
                        "FeaturedAliens": "Wildmutt, Diamondhead, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e01"
                    },
                    {
                        "Id": "classic-s02e02",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 2,
                        "Title": "The Big Tick",
                        "Description": "A colossal parasitic alien called the Great One threatens to consume Earth's energy. Ben unlocks Cannonbolt.",
                        "Duration": "22 min",
                        "AirDate": "May 30, 2006",
                        "FeaturedAliens": "Cannonbolt, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e02"
                    },
                    {
                        "Id": "classic-s02e03",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 3,
                        "Title": "Framed",
                        "Description": "In San Francisco, Ben is blamed for crimes actually committed by Kevin 11, who has absorbed all ten alien abilities.",
                        "Duration": "22 min",
                        "AirDate": "May 31, 2006",
                        "FeaturedAliens": "Four Arms, XLR8, Diamondhead",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e03"
                    },
                    {
                        "Id": "classic-s02e04",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 4,
                        "Title": "Gwen 10",
                        "Description": "Ben wakes up back at the first day of summer vacation, but this time Gwen finds the Omnitrix instead of him.",
                        "Duration": "22 min",
                        "AirDate": "Jun 1, 2006",
                        "FeaturedAliens": "Heatblast, Diamondhead, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e04"
                    },
                    {
                        "Id": "classic-s02e05",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 5,
                        "Title": "Grudge Match",
                        "Description": "Ben and Kevin are captured by Slix Vigma and forced into gladiatorial combat aboard a massive alien arena ship.",
                        "Duration": "22 min",
                        "AirDate": "Jun 7, 2006",
                        "FeaturedAliens": "Four Arms, Cannonbolt, Upgrade",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e05"
                    },
                    {
                        "Id": "classic-s02e06",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 6,
                        "Title": "The Galactic Enforcers",
                        "Description": "Ben teams up with an interstellar trio of goofy heroes to battle Bounty Hunter Sixsix and Vulkanus.",
                        "Duration": "22 min",
                        "AirDate": "Jun 13, 2006",
                        "FeaturedAliens": "Diamondhead, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e06"
                    },
                    {
                        "Id": "classic-s02e07",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 7,
                        "Title": "Camp Fear",
                        "Description": "At a weird summer camp, mushroom spore creatures called Mycelium invade, prompting Ben to unlock Wildvine.",
                        "Duration": "22 min",
                        "AirDate": "Jun 21, 2006",
                        "FeaturedAliens": "Wildvine, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e07"
                    },
                    {
                        "Id": "classic-s02e08",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 8,
                        "Title": "Ultimate Weapon",
                        "Description": "Grandpa Max becomes obsessed with recovering the Sword of Ek Chuaj before the sinister Forever Knights get it.",
                        "Duration": "22 min",
                        "AirDate": "Jul 6, 2006",
                        "FeaturedAliens": "Four Arms, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e08"
                    },
                    {
                        "Id": "classic-s02e09",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 9,
                        "Title": "Tough Luck",
                        "Description": "Hex breaks out of prison aided by his niece Charmcaster, seeking the Keystone of Bezel in Las Vegas.",
                        "Duration": "22 min",
                        "AirDate": "Jul 12, 2006",
                        "FeaturedAliens": "Wildvine, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e09"
                    },
                    {
                        "Id": "classic-s02e10",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 10,
                        "Title": "They Lurk Below",
                        "Description": "A billionaire's high-tech submarine is sabotaged by strange underwater aliens during a deep-sea trench expedition.",
                        "Duration": "22 min",
                        "AirDate": "Jul 18, 2006",
                        "FeaturedAliens": "Ripjaws, Upgrade",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e10"
                    },
                    {
                        "Id": "classic-s02e11",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 11,
                        "Title": "Ghostfreaked Out",
                        "Description": "Ghostfreak breaks free from the Omnitrix, shedding his outer skin to reveal his true terrifying form, Zs'Skayr.",
                        "Duration": "22 min",
                        "AirDate": "Jul 25, 2006",
                        "FeaturedAliens": "Four Arms, Grey Matter, Sun-Powered Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e11"
                    },
                    {
                        "Id": "classic-s02e12",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 12,
                        "Title": "Doctor of the Year",
                        "Description": "Ben faces off against Dr. Animo once again as he attempts to genetically engineer hyper-evolved mutant insect armies.",
                        "Duration": "22 min",
                        "AirDate": "Aug 25, 2006",
                        "FeaturedAliens": "Stinkfly, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e12"
                    },
                    {
                        "Id": "classic-s02e13",
                        "UniverseId": "classic",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 13,
                        "Title": "Back with a Vengeance",
                        "Description": "Ben discovers the Master Control of the Omnitrix, granting instant alien transformations, just as Vilgax and Kevin 11 ally against him.",
                        "Duration": "23 min",
                        "AirDate": "Oct 9, 2006",
                        "FeaturedAliens": "All 10 Original Aliens + Cannonbolt, Wildvine",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s02e13"
                    }
                ]
            },
            {
                "SeasonNumber": 3,
                "Title": "Season 3",
                "ReleaseYear": "2006 - 2007",
                "Description": "Ben battles alien horrors from the Anur system, journeys into the future, and confronts Zs'Skayr's dark master plan.",
                "Episodes": [
                    {
                        "Id": "classic-s03e01",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 1,
                        "Title": "Ben 10,000",
                        "Description": "Ben and Gwen are pulled 20 years into the future by Gwendolyn, meeting an adult, hardened Ben 10,000 who commands 10,000 aliens.",
                        "Duration": "23 min",
                        "AirDate": "Nov 25, 2006",
                        "FeaturedAliens": "Spitter, Buzzshock, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e01"
                    },
                    {
                        "Id": "classic-s03e02",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 2,
                        "Title": "Midnight Madness",
                        "Description": "A stage hypnotist named Sublimino uses sleepwalking mall shoppers to pull off massive bank heists.",
                        "Duration": "22 min",
                        "AirDate": "Dec 2, 2006",
                        "FeaturedAliens": "Upgrade, Wildmutt",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e02"
                    },
                    {
                        "Id": "classic-s03e03",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 3,
                        "Title": "A Change of Face",
                        "Description": "Charmcaster body-swaps with Ben using a mystical spell, aiming to possess the Omnitrix forever.",
                        "Duration": "22 min",
                        "AirDate": "Dec 9, 2006",
                        "FeaturedAliens": "Cannonbolt, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e03"
                    },
                    {
                        "Id": "classic-s03e04",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 4,
                        "Title": "Merry Christmas",
                        "Description": "In a bizarre desert oasis, an eccentric elf-obsessed man turns everyone into festive helpers.",
                        "Duration": "22 min",
                        "AirDate": "Dec 11, 2006",
                        "FeaturedAliens": "Four Arms, Stinkfly",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e04"
                    },
                    {
                        "Id": "classic-s03e05",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 5,
                        "Title": "Benwolf",
                        "Description": "In New Mexico, an alien werewolf attacks. When scratched, Ben undergoes a transformation into Blitzwolfer.",
                        "Duration": "22 min",
                        "AirDate": "Feb 17, 2007",
                        "FeaturedAliens": "Blitzwolfer (Benwolf), Wildvine",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e05"
                    },
                    {
                        "Id": "classic-s03e06",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 6,
                        "Title": "Game Over",
                        "Description": "Ben and Gwen are sucked inside a Sumo Slammers video game and must level up to escape.",
                        "Duration": "22 min",
                        "AirDate": "Feb 24, 2007",
                        "FeaturedAliens": "Upgrade, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e06"
                    },
                    {
                        "Id": "classic-s03e07",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 7,
                        "Title": "Super Alien Hero Buddy Adventures",
                        "Description": "Ben is furious to discover a cheap animated Saturday morning TV show copying his alien heroes.",
                        "Duration": "22 min",
                        "AirDate": "Mar 3, 2007",
                        "FeaturedAliens": "Four Arms, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e07"
                    },
                    {
                        "Id": "classic-s03e08",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 8,
                        "Title": "Under Wraps",
                        "Description": "Grandpa Max takes Ben and Gwen to a farm, where an alien Mummy begins mining dangerous Corrodium.",
                        "Duration": "22 min",
                        "AirDate": "Mar 10, 2007",
                        "FeaturedAliens": "Snare-oh (Benmummy), Upgrade",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e08"
                    },
                    {
                        "Id": "classic-s03e09",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 9,
                        "Title": "The Unnaturals",
                        "Description": "Ben attends a Little League baseball game and realizes the opposing team are robot synthetics trying to abduct officials.",
                        "Duration": "22 min",
                        "AirDate": "Mar 17, 2007",
                        "FeaturedAliens": "Four Arms, XLR8, Ripjaws",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e09"
                    },
                    {
                        "Id": "classic-s03e10",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 10,
                        "Title": "Monster Weather",
                        "Description": "A disgruntled ex-news weatherman builds a machine controlling storms and giant elemental weather monsters.",
                        "Duration": "22 min",
                        "AirDate": "Mar 24, 2007",
                        "FeaturedAliens": "Heatblast, Four Arms, XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e10"
                    },
                    {
                        "Id": "classic-s03e11",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 11,
                        "Title": "The Return",
                        "Description": "At NASA's Cape Canaveral, Doctor Vicktor and the Anur trio assemble a Corrodium transmission beam to awaken Ghostfreak.",
                        "Duration": "22 min",
                        "AirDate": "Apr 7, 2007",
                        "FeaturedAliens": "Frankenstrike (Benvicktor), XLR8",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e11"
                    },
                    {
                        "Id": "classic-s03e12",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 12,
                        "Title": "Be Afraid of the Dark",
                        "Description": "Ben travels to an orbital space station to stop Zs'Skayr from cloaking Earth in total darkness forever.",
                        "Duration": "23 min",
                        "AirDate": "Apr 14, 2007",
                        "FeaturedAliens": "Frankenstrike, Cannonbolt, Upchuck",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e12"
                    },
                    {
                        "Id": "classic-s03e13",
                        "UniverseId": "classic",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 13,
                        "Title": "The Visitor",
                        "Description": "An ancient alien friend of Grandpa Max, Xylene, arrives on Earth to find the Omnitrix she originally sent to him.",
                        "Duration": "22 min",
                        "AirDate": "Apr 21, 2007",
                        "FeaturedAliens": "Upchuck, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s03e13"
                    }
                ]
            },
            {
                "SeasonNumber": 4,
                "Title": "Season 4",
                "ReleaseYear": "2007 - 2008",
                "Description": "The climatic finale of the original summer journey, featuring the Forever King and the road back to Bellwood.",
                "Episodes": [
                    {
                        "Id": "classic-s04e01",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 1,
                        "Title": "Perfect Day",
                        "Description": "Ben experiences an unbelievable day where everything goes his way, only to realize he is trapped in a dream chamber created by the Forever Knights.",
                        "Duration": "22 min",
                        "AirDate": "Jul 14, 2007",
                        "FeaturedAliens": "Four Arms, XLR8, Diamondhead",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e01"
                    },
                    {
                        "Id": "classic-s04e02",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 2,
                        "Title": "Divided We Fall",
                        "Description": "Ben accidentally unlocks Ditto, a clone-capable alien, and must round up all his duplicates while stopping Dr. Animo from creating mutant clones.",
                        "Duration": "22 min",
                        "AirDate": "Jul 19, 2007",
                        "FeaturedAliens": "Ditto",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e02"
                    },
                    {
                        "Id": "classic-s04e03",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 3,
                        "Title": "Don't Drink the Water",
                        "Description": "Grandpa Max drinks from the Fountain of Youth and turns into a 10-year-old child, while Hex seeks eternal life.",
                        "Duration": "22 min",
                        "AirDate": "Jul 26, 2007",
                        "FeaturedAliens": "Heatblast (Toddler), Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e03"
                    },
                    {
                        "Id": "classic-s04e04",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 4,
                        "Title": "Big Fat Alien Wedding",
                        "Description": "Ben and his family attend a relative's wedding, where the bride's family are secretly alien mud-creatures called Sludgepuppies.",
                        "Duration": "22 min",
                        "AirDate": "Aug 2, 2007",
                        "FeaturedAliens": "Heatblast, Cannonbolt",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e04"
                    },
                    {
                        "Id": "classic-s04e05",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 5,
                        "Title": "Ben 4 Good Buddy",
                        "Description": "The Rustbucket is hijacked by a band of post-apocalyptic road pirates calling themselves the Road Crew.",
                        "Duration": "22 min",
                        "AirDate": "Sep 22, 2007",
                        "FeaturedAliens": "Wildvine, Upgrade",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e05"
                    },
                    {
                        "Id": "classic-s04e06",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 6,
                        "Title": "Ready to Rumble",
                        "Description": "To replace Gwen's broken laptop, Ben enters an underground wrestling circuit using his alien powers.",
                        "Duration": "22 min",
                        "AirDate": "Sep 29, 2007",
                        "FeaturedAliens": "Four Arms, Ditto",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e06"
                    },
                    {
                        "Id": "classic-s04e07",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 7,
                        "Title": "Ken 10",
                        "Description": "In the future, Ben 10,000 gives his 10-year-old son Ken an Omnitrix for his birthday, but Kevin Levin's son seeks revenge.",
                        "Duration": "23 min",
                        "AirDate": "Oct 6, 2007",
                        "FeaturedAliens": "Buzzshock, Spitter, Way Big",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e07"
                    },
                    {
                        "Id": "classic-s04e08",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 8,
                        "Title": "Ben 10 vs. The Negative 10 (Part 1)",
                        "Description": "The Forever King unites 10 of Ben's greatest foes to steal the Sub-Energy, the most powerful power source in the galaxy, from Mount Rushmore.",
                        "Duration": "23 min",
                        "AirDate": "Mar 9, 2008",
                        "FeaturedAliens": "Eye Guy, Upchuck, Cannonbolt",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e08"
                    },
                    {
                        "Id": "classic-s04e09",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 9,
                        "Title": "Ben 10 vs. The Negative 10 (Part 2)",
                        "Description": "Inside the Mount Rushmore Plumber base, Ben, Gwen, and Max fight the unified Negative 10 in an all-out battle.",
                        "Duration": "23 min",
                        "AirDate": "Mar 9, 2008",
                        "FeaturedAliens": "Eye Guy, Upchuck, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e09"
                    },
                    {
                        "Id": "classic-s04e10",
                        "UniverseId": "classic",
                        "SeasonNumber": 4,
                        "EpisodeNumber": 10,
                        "Title": "Goodbye and Good Riddance",
                        "Description": "Summer ends and Ben returns to school in Bellwood. Vilgax attacks his hometown, forcing Ben to reveal his secret identity to his father.",
                        "Duration": "23 min",
                        "AirDate": "Apr 15, 2008",
                        "FeaturedAliens": "Diamondhead, XLR8, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-classic-s04e10"
                    }
                ]
            }
        ]
    },
    {
        "Id": "alien-force",
        "Name": "Ben 10: Alien Force",
        "Tagline": "The War for Earth Begins",
        "Description": "Five years later, 15-year-old Ben Tennyson puts on the recalibrated Omnitrix to investigate Grandpa Max's disappearance and combat the genocidal Highbreed invasion.",
        "ReleaseYears": "2008 - 2010",
        "AccentColor": "#00ff41",
        "PosterClass": "alien-force",
        "BannerImage": "/images/alien-force-banner.jpg",
        "Seasons": [
            {
                "SeasonNumber": 1,
                "Title": "Season 1",
                "ReleaseYear": "2008",
                "Description": "Ben recalibrates the Omnitrix, teams up with Gwen and reformed Kevin Levin, and uncovers the Highbreed plot.",
                "Episodes": [
                    {
                        "Id": "af-s01e01",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 1,
                        "Title": "Ben 10 Returns (Part 1)",
                        "Description": "Ben Tennyson, now 15, discovers Grandpa Max has vanished. Investigating an illegal alien tech ring leads to an encounter with Kevin Levin.",
                        "Duration": "22 min",
                        "AirDate": "Apr 18, 2008",
                        "FeaturedAliens": "Swampfire",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e01"
                    },
                    {
                        "Id": "af-s01e02",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 2,
                        "Title": "Ben 10 Returns (Part 2)",
                        "Description": "Ben, Gwen, and Kevin infiltrate a Forever Knight castle and face off against a Highbreed commander.",
                        "Duration": "22 min",
                        "AirDate": "Apr 18, 2008",
                        "FeaturedAliens": "Echo Echo, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e02"
                    },
                    {
                        "Id": "af-s01e03",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 3,
                        "Title": "Everybody Talks About the Weather",
                        "Description": "The team investigates sudden crop circles and blizzards, meeting Alan Albright, a half-human, half-Pyronite Plumber's kid.",
                        "Duration": "22 min",
                        "AirDate": "Apr 26, 2008",
                        "FeaturedAliens": "Swampfire, Jetray",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e03"
                    },
                    {
                        "Id": "af-s01e04",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 4,
                        "Title": "Kevin's Big Score",
                        "Description": "Kevin sells Grandpa Max's Rustbucket to his former associate Argit to buy an alien holoprojector.",
                        "Duration": "22 min",
                        "AirDate": "May 3, 2008",
                        "FeaturedAliens": "Echo Echo",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e04"
                    },
                    {
                        "Id": "af-s01e05",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 5,
                        "Title": "All That Glitters",
                        "Description": "Ben, Gwen, and Kevin cross paths with Michael Morningstar, a charming boy who secretly drains youth and life energy.",
                        "Duration": "22 min",
                        "AirDate": "May 10, 2008",
                        "FeaturedAliens": "Spidermonkey, Jetray",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e05"
                    },
                    {
                        "Id": "af-s01e06",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 6,
                        "Title": "Max Out",
                        "Description": "The team finds Grandpa Max inside an underground Highbreed DNAlien breeding factory.",
                        "Duration": "22 min",
                        "AirDate": "May 17, 2008",
                        "FeaturedAliens": "Brainstorm, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e06"
                    },
                    {
                        "Id": "af-s01e07",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 7,
                        "Title": "Pier Pressure",
                        "Description": "Ben goes on a date with Julie Yamamoto at an amusement park, only for a Galvanic Mechamorph pet named Ship to cause chaos.",
                        "Duration": "22 min",
                        "AirDate": "May 31, 2008",
                        "FeaturedAliens": "Brainstorm, Spidermonkey",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e07"
                    },
                    {
                        "Id": "af-s01e08",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 8,
                        "Title": "What Are Little Girls Made Of?",
                        "Description": "Gwen meets her grandmother Verdona, discovering the Tennyson family's magical alien lineage as Anodites.",
                        "Duration": "22 min",
                        "AirDate": "Jun 7, 2008",
                        "FeaturedAliens": "Swampfire",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e08"
                    },
                    {
                        "Id": "af-s01e09",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 9,
                        "Title": "The Gauntlet",
                        "Description": "School bully JT and cash get their hands on a discarded alien gauntlet that turns Cash into a metallic monster.",
                        "Duration": "22 min",
                        "AirDate": "Jun 14, 2008",
                        "FeaturedAliens": "Chromastone, Echo Echo",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e09"
                    },
                    {
                        "Id": "af-s01e10",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 10,
                        "Title": "Paradox",
                        "Description": "A 1950s military time-travel experiment goes wrong, unleashing a temporal anomaly and introducing the time traveler Professor Paradox.",
                        "Duration": "22 min",
                        "AirDate": "Jul 5, 2008",
                        "FeaturedAliens": "Humungousaur, Alien X (Preview)",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e10"
                    },
                    {
                        "Id": "af-s01e11",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 11,
                        "Title": "Be-Knighted",
                        "Description": "Forever Knight squire Connor requests Ben's assistance in slaying a real alien dragon held captive beneath a castle.",
                        "Duration": "22 min",
                        "AirDate": "Jul 12, 2008",
                        "FeaturedAliens": "Humungousaur, Spidermonkey",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e11"
                    },
                    {
                        "Id": "af-s01e12",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 12,
                        "Title": "Plumbers' Helpers",
                        "Description": "Ben, Gwen, and Kevin are ambushed by Plumber's kids Pierce and Helen, who mistakenly believe they are rogue aliens.",
                        "Duration": "22 min",
                        "AirDate": "Jul 19, 2008",
                        "FeaturedAliens": "Humungousaur, Jetray",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e12"
                    },
                    {
                        "Id": "af-s01e13",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 13,
                        "Title": "X = Ben + 2",
                        "Description": "When the Incursian warlord Attea kidnaps Emperor Milleous, Ben turns into Alien X to stop a planetary annihilation, but gets trapped in internal debate.",
                        "Duration": "23 min",
                        "AirDate": "Aug 31, 2008",
                        "FeaturedAliens": "Alien X, Swampfire",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s01e13"
                    }
                ]
            },
            {
                "SeasonNumber": 2,
                "Title": "Season 2",
                "ReleaseYear": "2008 - 2009",
                "Description": "The Highbreed armada reaches Earth for total extinction, leading to the legendary Battle of Galvan Prime and the cure.",
                "Episodes": [
                    {
                        "Id": "af-s02e01",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 1,
                        "Title": "Darkstar Rising",
                        "Description": "Michael Morningstar returns as Darkstar, rallying the team's greatest adversaries to exact vengeance.",
                        "Duration": "22 min",
                        "AirDate": "Oct 10, 2008",
                        "FeaturedAliens": "Humungousaur, Jetray",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e01"
                    },
                    {
                        "Id": "af-s02e02",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 2,
                        "Title": "Alone Together",
                        "Description": "Ben and a Highbreed commander named Reinrassic III are transported through a malfunctioning teleporter to a hostile desert world.",
                        "Duration": "22 min",
                        "AirDate": "Oct 17, 2008",
                        "FeaturedAliens": "Swampfire, Humungousaur, Echo Echo",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e02"
                    },
                    {
                        "Id": "af-s02e03",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 3,
                        "Title": "Good Copy, Bad Copy",
                        "Description": "Albedo, a disgruntled Galvan assistant to Azmuth, builds his own Omnitrix but gets permanently trapped in Ben's human form.",
                        "Duration": "22 min",
                        "AirDate": "Oct 24, 2008",
                        "FeaturedAliens": "Goop, Spidermonkey, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e03"
                    },
                    {
                        "Id": "af-s02e04",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 4,
                        "Title": "Save the Last Dance",
                        "Description": "Ben experiences involuntary transformations into Big Chill during his sleep, discovering the alien is preparing to reproduce.",
                        "Duration": "22 min",
                        "AirDate": "Nov 7, 2008",
                        "FeaturedAliens": "Big Chill",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e04"
                    },
                    {
                        "Id": "af-s02e05",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 5,
                        "Title": "Undercover",
                        "Description": "Ben, Gwen, and Kevin track a Highbreed supply line to a teleporter tower guarded by DNAliens.",
                        "Duration": "22 min",
                        "AirDate": "Nov 14, 2008",
                        "FeaturedAliens": "Echo Echo, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e05"
                    },
                    {
                        "Id": "af-s02e06",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 6,
                        "Title": "Pet Project",
                        "Description": "The Forever Knights kidnap Ship to use his Galvanic Mechamorph abilities to construct a starship capable of destroying the dragon home world.",
                        "Duration": "22 min",
                        "AirDate": "Nov 21, 2008",
                        "FeaturedAliens": "Swampfire, Jetray",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e06"
                    },
                    {
                        "Id": "af-s02e07",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 7,
                        "Title": "Ground Zero",
                        "Description": "The team must disable a colossal Highbreed warp gate before the main battle fleet can arrive in Earth's solar system.",
                        "Duration": "22 min",
                        "AirDate": "Dec 5, 2008",
                        "FeaturedAliens": "Brainstorm, Goop",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e07"
                    },
                    {
                        "Id": "af-s02e08",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 8,
                        "Title": "War of the Worlds (Part 1)",
                        "Description": "The Highbreed armada enters Earth's orbit. Ben rallies all Plumber's kids, former enemies, and allies for the decisive showdown.",
                        "Duration": "23 min",
                        "AirDate": "Mar 27, 2009",
                        "FeaturedAliens": "Cannonbolt, Upchuck, Way Big",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e08"
                    },
                    {
                        "Id": "af-s02e09",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 9,
                        "Title": "War of the Worlds (Part 2)",
                        "Description": "Ben reprograms the Omnitrix to rewrite the Highbreed's damaged genetic code, ending the war and bringing galactic peace.",
                        "Duration": "24 min",
                        "AirDate": "Mar 27, 2009",
                        "FeaturedAliens": "Alien X, Swampfire, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s02e09"
                    }
                ]
            },
            {
                "SeasonNumber": 3,
                "Title": "Season 3",
                "ReleaseYear": "2009 - 2010",
                "Description": "Vilgax returns with the power of ten conquered champions, and the creation of the Ultimatrix changes everything.",
                "Episodes": [
                    {
                        "Id": "af-s03e01",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 1,
                        "Title": "Vengeance of Vilgax (Part 1)",
                        "Description": "Vilgax challenges the champions of worlds and claims their powers under galactic law, demanding a formal duel with Earth's protector, Ben Tennyson.",
                        "Duration": "23 min",
                        "AirDate": "Sep 11, 2009",
                        "FeaturedAliens": "Chromastone, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s03e01"
                    },
                    {
                        "Id": "af-s03e02",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 2,
                        "Title": "Vengeance of Vilgax (Part 2)",
                        "Description": "Ben hacks the Omnitrix with Kevin to unlock Master Control, causing a catastrophic overload that alters Kevin's body into composite armor.",
                        "Duration": "23 min",
                        "AirDate": "Sep 11, 2009",
                        "FeaturedAliens": "Diamondhead (Reconstructed), Lodestar",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s03e02"
                    },
                    {
                        "Id": "af-s03e03",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 3,
                        "Title": "Inferno",
                        "Description": "Beneath the desert sands, Pyronites are blamed for stealing water until Ben discovers a subterranean Pyroxivore race.",
                        "Duration": "22 min",
                        "AirDate": "Sep 18, 2009",
                        "FeaturedAliens": "Humungousaur, Big Chill",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s03e03"
                    },
                    {
                        "Id": "af-s03e04",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 4,
                        "Title": "Simple",
                        "Description": "Ben intervenes in a centuries-long war between two alien factions fighting over the color of their respective uniforms.",
                        "Duration": "22 min",
                        "AirDate": "Sep 25, 2009",
                        "FeaturedAliens": "Lodestar, Upchuck",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s03e04"
                    },
                    {
                        "Id": "af-s03e05",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 5,
                        "Title": "The Final Battle (Part 1)",
                        "Description": "Albedo steals the Ultimatrix and joins forces with Vilgax, capturing Gwen and Kevin to force Ben into surrender.",
                        "Duration": "23 min",
                        "AirDate": "Mar 26, 2010",
                        "FeaturedAliens": "Ultimate Humungousaur (Albedo), Swampfire",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s03e05"
                    },
                    {
                        "Id": "af-s03e06",
                        "UniverseId": "alien-force",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 6,
                        "Title": "The Final Battle (Part 2)",
                        "Description": "Ben triggers the Omnitrix's self-destruct command to prevent Vilgax from conquering the universe, then claims the Ultimatrix from Albedo.",
                        "Duration": "24 min",
                        "AirDate": "Mar 26, 2010",
                        "FeaturedAliens": "Ultimate Swampfire, Ultimatrix",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-af-s03e06"
                    }
                ]
            }
        ]
    },
    {
        "Id": "ultimate-alien",
        "Name": "Ben 10: Ultimate Alien",
        "Tagline": "Evolved Power Revealed",
        "Description": "Ben wields the Ultimatrix, granting him the power to evolve his aliens into hyper-powerful Ultimate forms while dealing with worldwide fame after his identity is leaked.",
        "ReleaseYears": "2010 - 2012",
        "AccentColor": "#00d2ff",
        "PosterClass": "ultimate-alien",
        "BannerImage": "/images/ultimate-alien-banner.jpg",
        "Seasons": [
            {
                "SeasonNumber": 1,
                "Title": "Season 1",
                "ReleaseYear": "2010",
                "Description": "Young Jimmy Jones leaks Ben's identity to the world. Aggregor searches for the five Andromeda aliens to reach the Forge of Creation.",
                "Episodes": [
                    {
                        "Id": "ua-s01e01",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 1,
                        "Title": "Fame",
                        "Description": "Ben's secret superhero identity is revealed to the world by young internet blogger Jimmy Jones, turning him into an instant global celebrity.",
                        "Duration": "22 min",
                        "AirDate": "Apr 23, 2010",
                        "FeaturedAliens": "Ultimate Spidermonkey, Humungousaur",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e01"
                    },
                    {
                        "Id": "ua-s01e02",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 2,
                        "Title": "Duped",
                        "Description": "Ben divides himself into three using Echo Echo to simultaneously attend Julie's tennis match, a movie premiere, and fight the Forever Knights.",
                        "Duration": "22 min",
                        "AirDate": "Apr 30, 2010",
                        "FeaturedAliens": "Echo Echo, Ultimate Echo Echo",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e02"
                    },
                    {
                        "Id": "ua-s01e03",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 3,
                        "Title": "Hit 'Em Where They Live",
                        "Description": "With Ben's identity public, villains Zombozo, Charmcaster, and Vulkanus target Ben's parents Sandra and Carl.",
                        "Duration": "22 min",
                        "AirDate": "May 7, 2010",
                        "FeaturedAliens": "Ultimate Big Chill, Big Chill",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e03"
                    },
                    {
                        "Id": "ua-s01e04",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 4,
                        "Title": "Video Games",
                        "Description": "Ben agrees to do motion-capture for a video game, but the developer uses the data to construct a combat robot called the Stalker.",
                        "Duration": "22 min",
                        "AirDate": "May 14, 2010",
                        "FeaturedAliens": "Nanomech, Ultimate Humungousaur, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e04"
                    },
                    {
                        "Id": "ua-s01e05",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 5,
                        "Title": "Escape from Aggregor",
                        "Description": "Five alien refugees from the Andromeda Galaxy crash-land on Earth while fleeing the ruthless Osmosian warlord Aggregor.",
                        "Duration": "22 min",
                        "AirDate": "May 21, 2010",
                        "FeaturedAliens": "Terraspin (Galapagus), Water Hazard",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e05"
                    },
                    {
                        "Id": "ua-s01e06",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 6,
                        "Title": "Too Hot to Handle",
                        "Description": "P'andor, a radioactive energy being encased in armored containment suit, tries to crack open his shell using radioactive isotopes.",
                        "Duration": "22 min",
                        "AirDate": "May 28, 2010",
                        "FeaturedAliens": "NRG, Ultimate Swampfire",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e06"
                    },
                    {
                        "Id": "ua-s01e07",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 7,
                        "Title": "Andreas' Fault",
                        "Description": "Argit convinces Andreas, a gentle Talpaedan who causes seismic earthquakes, that he is a divine leader of the Forever Knights.",
                        "Duration": "22 min",
                        "AirDate": "Jun 4, 2010",
                        "FeaturedAliens": "Armodrillo, Cannonbolt",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e07"
                    },
                    {
                        "Id": "ua-s01e08",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 8,
                        "Title": "Fused",
                        "Description": "Ra'ad, an Amperi electro-kinetic alien, merges into the Ultimatrix and takes possession of Ben's body to evade Aggregor.",
                        "Duration": "22 min",
                        "AirDate": "Jun 11, 2010",
                        "FeaturedAliens": "AmpFibian, Brainstorm",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e08"
                    },
                    {
                        "Id": "ua-s01e09",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 9,
                        "Title": "The Forge of Creation",
                        "Description": "Professor Paradox brings 16-year-old Ben and 10-year-old Ben together in the birthplace of Celestialsapiens to halt Aggregor.",
                        "Duration": "23 min",
                        "AirDate": "Nov 12, 2010",
                        "FeaturedAliens": "Ultimate Echo Echo, Alien X",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e09"
                    },
                    {
                        "Id": "ua-s01e10",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 10,
                        "Title": "Absolute Power (Part 2)",
                        "Description": "To save the galaxy from Aggregor, Kevin absorbs the Ultimatrix aliens and goes insane with power, forcing Ben to face him in a heartbreaking duel.",
                        "Duration": "24 min",
                        "AirDate": "Dec 10, 2010",
                        "FeaturedAliens": "Ultimate Echo Echo, Ultimate Spidermonkey",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s01e10"
                    }
                ]
            },
            {
                "SeasonNumber": 2,
                "Title": "Season 2",
                "ReleaseYear": "2011",
                "Description": "The mystery of the Dagon, Sir George, and the Lucubra begins to threaten reality itself.",
                "Episodes": [
                    {
                        "Id": "ua-s02e01",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 1,
                        "Title": "The Transmogrification of Eunice",
                        "Description": "Ben, Gwen, and Kevin find a crashed Galvan pod containing Eunice, an artificial genetic prototype of the Omnitrix called the Unitrix.",
                        "Duration": "22 min",
                        "AirDate": "Feb 4, 2011",
                        "FeaturedAliens": "Humungousaur, Rath",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s02e01"
                    },
                    {
                        "Id": "ua-s02e02",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 2,
                        "Title": "Eye of the Beholder",
                        "Description": "Ship leaves Earth suddenly to save his former Galvan creator Baz-El, prompting Julie and Ben to journey to his home world.",
                        "Duration": "22 min",
                        "AirDate": "Feb 11, 2011",
                        "FeaturedAliens": "Lodestar, Upchuck",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s02e02"
                    },
                    {
                        "Id": "ua-s02e03",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 3,
                        "Title": "Viktor: The Spoils",
                        "Description": "In a war-torn Eastern European nation, the prince resurrects the body of Doctor Viktor as a military super-weapon.",
                        "Duration": "22 min",
                        "AirDate": "Feb 18, 2011",
                        "FeaturedAliens": "Amphibian, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s02e03"
                    },
                    {
                        "Id": "ua-s02e04",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 4,
                        "Title": "The Creature from Beyond",
                        "Description": "The Forever Knights inadvertently break an ancient seal, freeing an extradimensional parasitic horror known as a Lucubra.",
                        "Duration": "22 min",
                        "AirDate": "Mar 25, 2011",
                        "FeaturedAliens": "Four Arms, Ultimate Spidermonkey",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s02e04"
                    },
                    {
                        "Id": "ua-s02e05",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 5,
                        "Title": "Basic Training",
                        "Description": "Ben, Gwen, and Kevin are summoned to the Plumbers' Academy in deep space for mandatory recruit training under drill instructor Magister Hulka.",
                        "Duration": "22 min",
                        "AirDate": "Apr 1, 2011",
                        "FeaturedAliens": "Fasttrack, Ripjaws",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s02e05"
                    },
                    {
                        "Id": "ua-s02e06",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 6,
                        "Title": "The Purge",
                        "Description": "The Forever Knights, united under the mysterious Old George, issue an ultimatum for all extraterrestrials to evacuate Earth or face annihilation.",
                        "Duration": "22 min",
                        "AirDate": "Sep 16, 2011",
                        "FeaturedAliens": "Way Big, Ultimate Echo Echo",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s02e06"
                    }
                ]
            },
            {
                "SeasonNumber": 3,
                "Title": "Season 3",
                "ReleaseYear": "2011 - 2012",
                "Description": "The final war against the interdimensional demon Dagon, and Azmuth's gifting of the definitive Omnitrix.",
                "Episodes": [
                    {
                        "Id": "ua-s03e01",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 1,
                        "Title": "The Ultimate Sacrifice",
                        "Description": "The sentient Ultimate forms trapped inside the Ultimatrix stage an uprising, demanding their freedom and threatening Ben's consciousness.",
                        "Duration": "22 min",
                        "AirDate": "Oct 28, 2011",
                        "FeaturedAliens": "Ultimate Humungousaur, Ultimate Cannonbolt",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s03e01"
                    },
                    {
                        "Id": "ua-s03e02",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 2,
                        "Title": "A Knight to Remember",
                        "Description": "Sir George leads the Forever Knights into the seal of Dagon, while Vilgax emerges as the Herald of Dagon.",
                        "Duration": "22 min",
                        "AirDate": "Feb 11, 2012",
                        "FeaturedAliens": "Eatle, Clockwork",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s03e02"
                    },
                    {
                        "Id": "ua-s03e03",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 3,
                        "Title": "Solitary Alignment",
                        "Description": "Azmuth reveals the origin of the Sword of Ascalon and how he first created it centuries ago to slay the cosmic beast Dagon.",
                        "Duration": "22 min",
                        "AirDate": "Feb 18, 2012",
                        "FeaturedAliens": "Clockwork, Azmuth",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s03e03"
                    },
                    {
                        "Id": "ua-s03e04",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 4,
                        "Title": "The Ultimate Enemy (Part 1)",
                        "Description": "Dagon breaks through the seal, brainwashing all humanity into Esoterica cultists. Sir George and Ben stand as the last line of defense.",
                        "Duration": "23 min",
                        "AirDate": "Mar 24, 2012",
                        "FeaturedAliens": "Ultimate Way Big, Ascalon Sword",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s03e04"
                    },
                    {
                        "Id": "ua-s03e05",
                        "UniverseId": "ultimate-alien",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 5,
                        "Title": "The Ultimate Enemy (Part 2)",
                        "Description": "Vilgax absorbs Dagon's powers to become a cosmic god. Ben uses Ascalon to defeat him, and Azmuth rewards Ben with the finished, official Omnitrix.",
                        "Duration": "25 min",
                        "AirDate": "Mar 31, 2012",
                        "FeaturedAliens": "Ascalon Armor, The New Omnitrix",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ua-s03e05"
                    }
                ]
            }
        ]
    },
    {
        "Id": "omniverse",
        "Name": "Ben 10: Omniverse",
        "Tagline": "Expanding the Multiverse",
        "Description": "Armed with the definitive Omnitrix and teamed up with rookie alien partner Rook Blonko, Ben explores the secret subterranean metropolis of Undertown and the wider multiverse.",
        "ReleaseYears": "2012 - 2014",
        "AccentColor": "#00ff41",
        "PosterClass": "omniverse",
        "BannerImage": "/images/omniverse-banner.jpg",
        "Seasons": [
            {
                "SeasonNumber": 1,
                "Title": "Arc 1: A New Beginning",
                "ReleaseYear": "2012",
                "Description": "Gwen and Kevin depart for college, leaving Ben partnered with straight-laced Plumber rookie Rook Blonko.",
                "Episodes": [
                    {
                        "Id": "ov-s01e01",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 1,
                        "Title": "The More Things Change (Part 1)",
                        "Description": "Ben is assigned a new Plumber partner, Rook Blonko, and investigates an alien shakedown racket in the hidden underground city of Undertown.",
                        "Duration": "22 min",
                        "AirDate": "Sep 22, 2012",
                        "FeaturedAliens": "Bloxx, Cannonbolt",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e01"
                    },
                    {
                        "Id": "ov-s01e02",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 2,
                        "Title": "The More Things Change (Part 2)",
                        "Description": "Ben and Rook track the mysterious predator alien hound and its hunter master Khyber, who wields the predatory Nemetrix.",
                        "Duration": "22 min",
                        "AirDate": "Sep 22, 2012",
                        "FeaturedAliens": "Shocksquatch, Gravattack",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e02"
                    },
                    {
                        "Id": "ov-s01e03",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 3,
                        "Title": "A Jolt from the Past",
                        "Description": "The Megawhatts from Sparksville return, trapped inside a battery powering a carnival, seeking Ben's help to free their kindred.",
                        "Duration": "22 min",
                        "AirDate": "Sep 29, 2012",
                        "FeaturedAliens": "Feedback, Shocksquatch",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e03"
                    },
                    {
                        "Id": "ov-s01e04",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 4,
                        "Title": "Trouble Helix",
                        "Description": "In a flashback to when Ben was 11, we witness the origin of Malware, a corrupted Galvanic Mechamorph who despises Azmuth.",
                        "Duration": "22 min",
                        "AirDate": "Oct 6, 2012",
                        "FeaturedAliens": "Heatblast, XLR8, Upgrade",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e04"
                    },
                    {
                        "Id": "ov-s01e05",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 5,
                        "Title": "Have I Got a Deal for You",
                        "Description": "An energetic alien salesman introduces a cuddly creature called the Screegit, which unexpectedly mutates when fed dairy.",
                        "Duration": "22 min",
                        "AirDate": "Oct 13, 2012",
                        "FeaturedAliens": "Ball Weevil, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e05"
                    },
                    {
                        "Id": "ov-s01e06",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 6,
                        "Title": "It Was Them",
                        "Description": "Dr. Animo escapes from the Plumbers' maximum security prison using mutant ants, while Khyber watches Ben's every tactical move.",
                        "Duration": "22 min",
                        "AirDate": "Oct 20, 2012",
                        "FeaturedAliens": "Crashhopper, Stinkfly",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e06"
                    },
                    {
                        "Id": "ov-s01e07",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 7,
                        "Title": "So Long, and Thanks for All the Smoothies",
                        "Description": "The Annihilargh device detonates, obliterating the entire universe. Ben transforms into Alien X to rebuild the universe from scratch.",
                        "Duration": "22 min",
                        "AirDate": "Oct 27, 2012",
                        "FeaturedAliens": "Alien X",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e07"
                    },
                    {
                        "Id": "ov-s01e08",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 8,
                        "Title": "Hot Stretch",
                        "Description": "Ben and Rook follow a string of high-tech thefts into Undertown's underbelly, discovering an underground alien black-market ring.",
                        "Duration": "22 min",
                        "AirDate": "Nov 3, 2012",
                        "FeaturedAliens": "Heatblast, Eatle",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e08"
                    },
                    {
                        "Id": "ov-s01e09",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 9,
                        "Title": "Of Predators and Prey (Part 1)",
                        "Description": "Ben and Rook have a bitter argument, splitting up just as Khyber the Hunter strikes, capturing Ben with Nemetrix predators.",
                        "Duration": "23 min",
                        "AirDate": "Nov 10, 2012",
                        "FeaturedAliens": "Humungousaur, Feedback",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e09"
                    },
                    {
                        "Id": "ov-s01e10",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 10,
                        "Title": "Of Predators and Prey (Part 2)",
                        "Description": "Trapped on Khyber's starship, Ben must overcome the trauma of losing Feedback years ago to defeat Malware and Khyber.",
                        "Duration": "24 min",
                        "AirDate": "Nov 17, 2012",
                        "FeaturedAliens": "Feedback (Restored), Way Big",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s01e10"
                    }
                ]
            },
            {
                "SeasonNumber": 2,
                "Title": "Arc 2: Malware's Revenge",
                "ReleaseYear": "2013",
                "Description": "Malware attacks Galvan Prime with the mecha-suit, triggering the greatest battle for Azmuth's world.",
                "Episodes": [
                    {
                        "Id": "ov-s02e01",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 1,
                        "Title": "Outbreak",
                        "Description": "Dr. Psychobos sabotages the Omnitrix, causing random alien body part combinations whenever Ben transforms.",
                        "Duration": "22 min",
                        "AirDate": "Nov 24, 2012",
                        "FeaturedAliens": "Alien Mashups, Grey Matter",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s02e01"
                    },
                    {
                        "Id": "ov-s02e02",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 2,
                        "Title": "Showdown (Part 1)",
                        "Description": "The Faction attacks Galvan Prime. Malware merges with the Moon's defense systems to grow into a gargantuan monstrosity.",
                        "Duration": "23 min",
                        "AirDate": "Feb 9, 2013",
                        "FeaturedAliens": "Feedback, Way Big",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s02e02"
                    },
                    {
                        "Id": "ov-s02e03",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 3,
                        "Title": "Showdown (Part 2)",
                        "Description": "Ben confronts his deepest psychological scars, reclaiming Feedback and unleashing maximum energy to atomize Malware once and for all.",
                        "Duration": "24 min",
                        "AirDate": "Feb 16, 2013",
                        "FeaturedAliens": "Feedback, Helix Cannon",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s02e03"
                    }
                ]
            },
            {
                "SeasonNumber": 3,
                "Title": "Arc 3: Incursian Invasion & Beyond",
                "ReleaseYear": "2013 - 2014",
                "Description": "The militaristic Incursian Empire conquer Earth, leading to the Multiverse War with Ben 23 and Mad Ben.",
                "Episodes": [
                    {
                        "Id": "ov-s03e01",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 1,
                        "Title": "The Frogs of War (Part 1)",
                        "Description": "Emperor Milleous and Princess Attea launch a planetary invasion of Earth, forcing the Plumbers into hiding.",
                        "Duration": "23 min",
                        "AirDate": "Mar 16, 2013",
                        "FeaturedAliens": "Bullfrag, Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s03e01"
                    },
                    {
                        "Id": "ov-s03e02",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 2,
                        "Title": "The Frogs of War (Part 2)",
                        "Description": "Ben infiltrates the Incursian war fleet transformed as an Incursian soldier (Bullfrag) to overthrow the conquest.",
                        "Duration": "23 min",
                        "AirDate": "Mar 23, 2013",
                        "FeaturedAliens": "Bullfrag, Way Big",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s03e02"
                    },
                    {
                        "Id": "ov-s03e03",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 3,
                        "Title": "Store 23",
                        "Description": "Ben is thrown into an alternate dimension where he meets Ben 23, a spoiled rich celebrity version of himself who names aliens goofy things.",
                        "Duration": "22 min",
                        "AirDate": "Apr 6, 2013",
                        "FeaturedAliens": "Feedback, Shocksquatch, Bloxx",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s03e03"
                    },
                    {
                        "Id": "ov-s03e04",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 4,
                        "Title": "And Then There Was None",
                        "Description": "Vilgax uses the Chronosapien Time Bomb to wipe out every Ben Tennyson in the entire multiverse, leaving only the Omnitrix-less No-Watch Ben.",
                        "Duration": "23 min",
                        "AirDate": "Oct 18, 2014",
                        "FeaturedAliens": "Clockwork, Paradox, Multiverse Bens",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s03e04"
                    },
                    {
                        "Id": "ov-s03e05",
                        "UniverseId": "omniverse",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 5,
                        "Title": "A New Dawn",
                        "Description": "Maltruant attempts to initiate the Big Bang in his own image. Ben holds the Annihilargh energy with Feedback and cycles through all his aliens in the ultimate sequence.",
                        "Duration": "25 min",
                        "AirDate": "Nov 14, 2014",
                        "FeaturedAliens": "Feedback, Every Single Omnitrix Alien",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-ov-s03e05"
                    }
                ]
            }
        ]
    },
    {
        "Id": "reboot",
        "Name": "Ben 10 (Reboot)",
        "Tagline": "A New Generation's Hero",
        "Description": "A reimagined generation with high-octane adventures, Omni-Enhanced forms, Omni-Kix armor, and alien-busting mech tech.",
        "ReleaseYears": "2016 - 2021",
        "AccentColor": "#ff4b2b",
        "PosterClass": "reboot",
        "BannerImage": "/images/reboot-banner.jpg",
        "Seasons": [
            {
                "SeasonNumber": 1,
                "Title": "Season 1",
                "ReleaseYear": "2016 - 2017",
                "Description": "Ben, Gwen, and Grandpa Max hit the road in the Rustbucket encountering Steam Smythe, Maurice, and Vilgax.",
                "Episodes": [
                    {
                        "Id": "rb-s01e01",
                        "UniverseId": "reboot",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 1,
                        "Title": "The Water Filter",
                        "Description": "Ben battles alien water monsters and the Victorian steampunk inventor Steam Smythe during a trip to Niagara Falls.",
                        "Duration": "11 min",
                        "AirDate": "Oct 1, 2016",
                        "FeaturedAliens": "Cannonbolt, Overflow",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s01e01"
                    },
                    {
                        "Id": "rb-s01e02",
                        "UniverseId": "reboot",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 2,
                        "Title": "The Ring Leader",
                        "Description": "While attending a carnival, Ben must protect the prize pig from giant mutated circus animals created by Dr. Animo.",
                        "Duration": "11 min",
                        "AirDate": "Oct 1, 2016",
                        "FeaturedAliens": "Four Arms, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s01e02"
                    },
                    {
                        "Id": "rb-s01e03",
                        "UniverseId": "reboot",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 3,
                        "Title": "Riding the Storm Out",
                        "Description": "The Weatherheads, a trio of malfunctioning robotic meteorologists, seek to plunge the nation into an eternal blizzard.",
                        "Duration": "11 min",
                        "AirDate": "Oct 2, 2016",
                        "FeaturedAliens": "Shock Rock, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s01e03"
                    },
                    {
                        "Id": "rb-s01e04",
                        "UniverseId": "reboot",
                        "SeasonNumber": 1,
                        "EpisodeNumber": 4,
                        "Title": "Omni-Tricked (Part 4)",
                        "Description": "Vilgax emerges from deep space to retrieve the Omnitrix. Ben unlocks Gax and confronts Vilgax in an epic showdown.",
                        "Duration": "22 min",
                        "AirDate": "May 29, 2017",
                        "FeaturedAliens": "Gax, Upgrade, Diamondhead",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s01e04"
                    }
                ]
            },
            {
                "SeasonNumber": 2,
                "Title": "Season 2: Omni-Enhanced",
                "ReleaseYear": "2018",
                "Description": "The Omnitrix absorbs Fulmasian energy, unlocking Omni-Enhanced alien transformations with energized plasma armor.",
                "Episodes": [
                    {
                        "Id": "rb-s02e01",
                        "UniverseId": "reboot",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 1,
                        "Title": "Out to Launch",
                        "Description": "During a tour of a space flight center, Ben uses Omni-Enhanced Grey Matter to prevent a rocket disaster.",
                        "Duration": "11 min",
                        "AirDate": "Feb 19, 2018",
                        "FeaturedAliens": "Omni-Enhanced Grey Matter",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s02e01"
                    },
                    {
                        "Id": "rb-s02e02",
                        "UniverseId": "reboot",
                        "SeasonNumber": 2,
                        "EpisodeNumber": 2,
                        "Title": "Innervasion (Part 5)",
                        "Description": "High Override attempts to conquer Earth using the Fulmasian power grid. Ben leads an energized assault to restore freedom.",
                        "Duration": "22 min",
                        "AirDate": "Oct 26, 2018",
                        "FeaturedAliens": "Shock Rock, Omni-Enhanced Aliens",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s02e02"
                    }
                ]
            },
            {
                "SeasonNumber": 3,
                "Title": "Season 3: Omni-Kix Armor",
                "ReleaseYear": "2019 - 2020",
                "Description": "Ben unlocks robotic Omni-Kix exosuits for every alien to battle Kevin 11's bootleg AntiTrix.",
                "Episodes": [
                    {
                        "Id": "rb-s03e01",
                        "UniverseId": "reboot",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 1,
                        "Title": "Omni-Copped",
                        "Description": "Ben faces off against Kevin 11 who builds his own AntiTrix in his garage, producing dark corrupted alien copies.",
                        "Duration": "11 min",
                        "AirDate": "Feb 23, 2019",
                        "FeaturedAliens": "Omni-Kix Cannonbolt, Slapback",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s03e01"
                    },
                    {
                        "Id": "rb-s03e02",
                        "UniverseId": "reboot",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 2,
                        "Title": "Ben 10,010",
                        "Description": "In a dark distant future, an adult Ben comes out of retirement alongside young Ben to stop an alien invasion.",
                        "Duration": "45 min",
                        "AirDate": "Feb 20, 2021",
                        "FeaturedAliens": "Alien V, Omni-Kix Four Arms",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s03e02"
                    },
                    {
                        "Id": "rb-s03e03",
                        "UniverseId": "reboot",
                        "SeasonNumber": 3,
                        "EpisodeNumber": 3,
                        "Title": "Alien X-Tinction",
                        "Description": "A rogue Celestialsapien dimension-traveler begins hunting Bens across the multiverse. Ben teams up with Classic Ben, AF Ben, UA Ben, and Reboot Ben!",
                        "Duration": "45 min",
                        "AirDate": "Apr 11, 2021",
                        "FeaturedAliens": "Multiverse Bens, Ripjaws, Bloxx, Heatblast",
                        "TeraBoxUrl": "https://terabox.com/s/ben10-rb-s03e03"
                    }
                ]
            }
        ]
    }
]

os.makedirs("Data", exist_ok=True)
with open(os.path.join("Data", "episodes.json"), "w", encoding="utf-8") as f:
    json.dump(universes, f, indent=2, ensure_ascii=False)

print(f"Generated {len(universes)} universes successfully into Data/episodes.json")
