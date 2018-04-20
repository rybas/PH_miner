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
        for post in phc.get_todays_posts():
            name=post.name
            tagline=post.tagline
            urlLogo=post.screenshot_url
            urlProduct=post.redirect_url
            votes=post.votes_count
            coments=post.comments_count
            print('name: ', name)
            print('tagline', tagline)
            print('hunter:', post.user.name)
            print(post.current_user)
            with io.open('popular_YYYY-mm-dd.csv', 'w',newline='', encoding="utf-8") as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([name,tagline,urlLogo,urlProduct,votes,coments])


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
