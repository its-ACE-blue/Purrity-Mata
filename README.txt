Purrity Mata
============
Bilingual Estonian/English maths formula + exam-practice prototype (MA11-MA13).

Open index.html in a browser. Estonian is the default; the ET/EN toggle is always visible and your choice is remembered.

Contents
- New formula cards: circle & sector area, line through two points, general line form, area under a curve, area between curves.
- Practice questions now include "hard" tasks with step-by-step worked solutions.
- Search is bilingual and concept-aware; question results show the question text, and the first 9 matches are listed, with a "Show more" button for the rest.

Honest labelling
- Past-exam practice tasks are ORIGINAL exercises tied to an exam year/topic. The source link shows where the topic reference comes from; it is not a copy of the exam task.

Formulas (MathJax)
- Loads from vendor/mathjax/es5/ if present (offline), otherwise from the jsDelivr CDN. A notice appears if neither works.
- Run `python get_offline_assets.py` once (with internet) to install MathJax and the Mali font locally.

Scope
- Covered: MA11 probability & plane geometry, MA12 solid geometry, MA13 analytic geometry & integrals.
- Not yet: sequences, exponential/logarithmic functions, function analysis.

Font: the UI uses "Mali" (Google Fonts, loaded online; falls back to Comic Sans MS / system fonts offline). Formulas are still typeset by MathJax.

Exam links: past-exam practice is tagged per subtopic, so a topic page only lists tasks that genuinely match it.
Formulas: every formula card has a "What the letters mean" legend in both languages (search also finds formulas by these terms).
Search: question results open and highlight the exact question; "Show more" reveals further matches.

Hosting on GitHub Pages
- Upload the contents of this folder to a repo (index.html at the top level), then Settings > Pages > deploy from the main branch.
- Navigation uses #/ links, so it works on Pages without any server setup.
- Online hosting means MathJax and the Mali font load from their CDNs; get_offline_assets.py and vendor/ are optional and can be ignored or deleted.
