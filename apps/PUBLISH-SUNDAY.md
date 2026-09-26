# Publishing the student apps — Sunday checklist

1. Download the Google Form's upload folder from Drive to your computer.
2. Open every HTML file in a browser first. You are hosting it on your domain; make sure it's the app they pitched and nothing else.
3. Put `sort-apps.py` in the same folder as the downloaded files and run:

       python3 sort-apps.py

   It creates `apps/<slug>/index.html` for each file (slug from the filename — rename files to the app name first, e.g. `cita-facil.html`).
4. Edit `apps/index.html`: fill each card (app name, person, one sentence, squad, schools), point each button at the matching `<slug>/`, and add the WINNER tag to one card. Delete cards for tracks with no finalist file.
5. Drag the `apps` folder onto the GitHub uploader from inside the site folder. Wait two minutes. Open longbeachaihackathon.org/apps/ on your phone.
6. Recap post: link to /apps/, group photo, academy dates.
