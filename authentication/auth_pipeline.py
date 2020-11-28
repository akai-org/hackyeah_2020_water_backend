def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = response['picture']
    if url:
        user.profile.avatar_url = url
    else:
        user.profile.avatar_url = "https://akai.org.pl/img/logo.svg"
    user.save()


def get_name(backend, strategy, details, response, user=None, *args, **kwargs):
    user.first_name = response['given_name']
    user.last_name = response['family_name']
    user.save()
