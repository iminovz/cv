from django.shortcuts import render


def home(request):
    return render(request, "cv/home1.html")


# info_dict = {
#    'home': 'cv/home.html',
#    'cv': 'cv.html',
# }


# def get_info(request, about_me):
#    description = info_dict.get(about_me)
#    if description:
#        return render(request, "cv/home.html")
#    else:
#        pass
