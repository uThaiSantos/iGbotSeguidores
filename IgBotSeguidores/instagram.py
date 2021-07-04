# importacao
from instapy import InstaPy
from instapy import smart_run

# Credenciais
insta_username = 'seu usuario'  # <- enter username here
insta_password = 'sua senha'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_do_follow(True, percentage=100)
    session.set_dont_like(["tags1", "tags2"])

    # activity
    session.like_by_tags(["tags1", "tags2"], amount=10)

