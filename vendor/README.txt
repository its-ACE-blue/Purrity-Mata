For fully offline use, run once with internet:
  python get_offline_assets.py
This fills vendor/mathjax/es5 and fonts/. Manual alternative: copy the MathJax 3 "es5" folder to vendor/mathjax/es5/.
Without it the page falls back to the jsDelivr CDN and Google Fonts.
