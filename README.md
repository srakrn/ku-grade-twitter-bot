# KU-Grade-Notify

This is a Twitter bot notifying fot the grade announcement via Kasetsart University registration system. It runs on Python3.

## Usage

Install all dependencies with

```
pip3 install -r requirements.txt
```

and then set up the following login credentials at `credentials.py`:
* Nontri account username and password
* Twitter credentials (both for app and account)

After that, run `notify.py` in the background (we recommends `nohup` or `screen`.)
