# KU-Grade-Notify

This is a Twitter bot notifying fot the grade announcement via Kasetsart University registration system. It runs on Python3.

## Credits

The core of this bot (KU-Regis fetching system) is heavily modified from [mameaw14/ku-check-grade](https://github.com/mameaw14/ku-check-grade/). All credit goes to [@Mameaw14](https://twitter.com/Mameaw14).

## Usage

Install all dependencies with

```
pip3 install -r requirements.txt
```

and then set up the following login credentials at `credentials.py`:
* Nontri account username and password
* Twitter credentials (both for app and account)

After that, run `notify.py` in the background (we recommends `nohup` or `screen`.)
