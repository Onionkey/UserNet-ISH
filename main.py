import sys
import requests

SEARCH_URLS = {
    # Existing social media platforms
}

# Additional social media platforms
ADDITIONAL_PLATFORMS = {
    'Twitter': 'https://twitter.com/{}',
    'Facebook': 'https://www.facebook.com/{}',
    'Instagram': 'https://www.instagram.com/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'Pinterest': 'https://www.pinterest.com/{}',
    'Reddit': 'https://www.reddit.com/user/{}',
    'Tumblr': 'https://{}.tumblr.com',
    'Snapchat': 'https://www.snapchat.com/add/{}',
    'GitHub': 'https://github.com/{}',
    'YouTube': 'https://www.youtube.com/user/{}',
    'Twitch': 'https://www.twitch.tv/{}',
    'WhatsApp': 'https://api.whatsapp.com/send?phone={}',
    'WeChat': 'https://web.wechat.com/{}',
    'Line': 'https://line.me/ti/p/{}',
    'Telegram': 'https://t.me/{}',
    'Discord': 'https://discord.com/users/{}',
    'Medium': 'https://medium.com/@{}',
    'SoundCloud': 'https://soundcloud.com/{}',
    'Vimeo': 'https://vimeo.com/{}',
    'Flickr': 'https://www.flickr.com/people/{}',
    'Slack': 'https://{}.slack.com',
    'Dribbble': 'https://dribbble.com/{}',
    'Behance': 'https://www.behance.net/{}',
    'DeviantArt': 'https://www.deviantart.com/{}',
    'Mixcloud': 'https://www.mixcloud.com/{}',
    'Goodreads': 'https://www.goodreads.com/user/show/{}',
    'Quora': 'https://www.quora.com/profile/{}',
}

# Combine the existing and additional platforms
SEARCH_URLS.update(ADDITIONAL_PLATFORMS)


def check_username_availability(username):
    if not username:
        print("Please enter a username.")
        return

    for platform, search_url in SEARCH_URLS.items():
        url = search_url.format(username)
        exists = check_username_exists(url)

        print(f"{platform}:")
        if exists:
            print("Username exists")
        else:
            print("Username does not exist")
        print(f"URL: {url}")
        print()


def check_username_exists(url):
    try:
        response = requests.head(url)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False


def display_ascii_art():
    ascii_art = """
          _   _             _  _     _   
         | | | |___ ___ _ _| \| |___| |_ 
         | |_| (_-</ -_) '_| .` / -_)  _|
          \___//__/\___|_| |_|\_\___|\__|
    """
    print(ascii_art)


if __name__ == '__main__':
    display_ascii_art()

    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    check_username_availability(username)
    print("Exiting...")
