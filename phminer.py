import os
import csv
import yaml
import io
from ph_py import ProductHuntClient
from ph_py.error import ProductHuntError

config_file = 'credentials.yml'

def run(key, secret, uri, token):
    phc = ProductHuntClient(key, secret, uri, token)
    # Example request
    try:
        with io.open('popular_YYYY-mm-dd.csv', 'w', newline='', encoding="utf-8") as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_ALL)
            for post in phc.get_todays_posts():
                name=post.name
                tagline=post.tagline
                urlLogo=post.screenshot_url
                urlProduct=post.redirect_url
                votes=post.votes_count
                coments=post.comments_count
                hunter=post.user.name
                hunterlink=post.user.profile_url
                coment= post.comments
                print('name: ', name)
                print('tagline :', tagline)
                print('hunter :', hunter)
                print('hunterlink :',hunterlink)
                spamwriter.writerow([name, tagline, urlLogo, urlProduct, votes, coments])

            print(post.current_user)



    except ProductHuntError as e:
        print(e.error_message)
        print(e.status_code)


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), config_file), 'r') as config:
        cfg = yaml.load(config)
        client_key = cfg['api']['key']
        client_secret = cfg['api']['secret']
        redirect_uri = cfg['api']['redirect_uri']
        dev_token = cfg['api']['dev_token']

    run(client_key, client_secret, redirect_uri, dev_token)
