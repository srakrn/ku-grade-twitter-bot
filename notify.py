import time
import random
import kuregis
import tweepy
import credentials
import re

def clean_string(string):
    """
    cleans a string, removing all whitespaces
    """
    return re.sub(r'\s+', '', string)

def changed(a, b):
    """
    compares string a to b
    """
    if clean_string(a) != clean_string(b): 
        return True
    return False

def process_html(raw_html):
    """
    remove unwanted HTML components (e.g. encoding)
    """
    raw_htmls = raw_html.splitlines()
    cooked = ""
    for html in raw_htmls:
        if "charset=" not in html:
            cooked += html+"\n"
    return cooked

def main():
    if not kuregis.login(credentials.ku_username, credentials.ku_password):
        print("Authentication failed.")
        return
    else:
        print("Authentication success.")

    auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_secret)
    auth.set_access_token(credentials.token_key, credentials.token_secret)
    api = tweepy.API(auth)

    ku20_html = kuregis.get_ku20_html()
    while True:
        try:
            f = open("ku20.html", "r")
            if changed(f.read(), ku20_html):
                api.update_status("@srakrn [BOT] เกรดออก cc @merunne_ @AyumiizZ @seashellx_")
                print("Changes found.")
        except OSError:
            print("First pulling.")
        f = open("index.html", "w")
        f.write(process_html(ku20_html))
        f.close()
        time.sleep(random.randint(120, 300))

if __name__ == "__main__":
    main()
