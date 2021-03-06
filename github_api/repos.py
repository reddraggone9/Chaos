import settings

def get_num_watchers(api, urn):
    """ returns the number of watchers for a repo """
    path = "/repos/{urn}".format(urn=urn)
    data = api("get", path)
    # this is the field for watchers.  do not be tricked by "watchers_count"
    # which always matches "stargazers_count"
    return data["subscribers_count"]


def set_desc(api, urn, desc):
    """ Set description and homepage of repo """
    path = "/repos/{urn}".format(urn=urn)
    data = {
        "name": settings.GITHUB_REPO,
        "description": desc,
        "homepage": settings.HOMEPAGE,
    }
    api("patch", path, json=data)
