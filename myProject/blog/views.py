from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# home page

def home(request):
    context = {
        "articles":[
            {
                "title": "One Punch Man",
                "description": "The seemingly ordinary and unimpressive Saitama has a rather unique hobby: being a hero. In order to pursue his childhood dream, he trained relentlessly for three years—and lost all of his hair in the process.",
                "img": "https://animelist.pw/public/storage/anime/image/2019/5/1556893725-c9261bbb.jpg"
            },
            {
                "title": "Shingeki no Kyojin",
                "description": "Centuries ago, mankind was slaughtered to near extinction by monstrous humanoid creatures called titans, forcing humans to hide in fear behind enormous concentric walls.",
                "img": "https://animelist.pw/public/storage/anime/image/2019/5/1556818737-6a418682.jpg"
            },
            {
                "title": "Yakusoku no Neverland",
                "description": "Surrounded by a forest and a gated entrance, the Grace Field House is inhabited by orphans happily living together as one big family, looked after by their Mama, Isabella. Although they are required to take tests daily, the children are free to spend their time as they see fit, usually playing outside, as long as they do not venture too far from the orphanage—a rule they are expected to follow no matter what.",
                "img": "https://animelist.pw/public/storage/anime/image/2019/5/1556669835-4f1ad7a2.jpg"
            }
        ]
    }
    return render(request, "blog/home.html", context)
