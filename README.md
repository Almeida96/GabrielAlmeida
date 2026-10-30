# Gabriel Almeida — athlete website

[![CI](https://github.com/Almeida96/GabrielAlmeida/actions/workflows/ci.yml/badge.svg)](https://github.com/Almeida96/GabrielAlmeida/actions/workflows/ci.yml)

A static portfolio for Brazilian Jiu Jitsu athlete Gabriel Almeida, with biography, sponsors, competition results and contact links. The site's content and assets live in [template/](template/).

## Preview

Requires Python 3 only for the local server:

```sh
python -m http.server 8000 --directory template
```

Open `http://localhost:8000`. Any static host can serve the contents of `template/`; no PHP server or build step is required.

## Contact behavior

The email button opens the visitor's email application. The old form did not submit its input correctly and could report success without delivering mail; that form and its PHP endpoint have been removed. The email links now match the address already displayed on the page.

## Maintain the site

- Edit visible content in `template/index.html`.
- Keep images under `template/images/` and preserve filename case for Linux hosting.
- Site styles are in `template/css/main.css` and `responsive.css`; interactions are in `template/js/main.js`.
- Run `python scripts/check_site.py` to check the main page's local links and assets.
- Preview the contact link, keyboard navigation and mobile layout before publishing.

The older `index teste.html` and `portfolio-single.html` files are retained as legacy template material; `template/index.html` is the supported entry point. Vendor libraries retain their existing notices. Photography, athlete information and sponsor logos are not granted a new reuse license by this documentation.

The existing Google Analytics tag and hosted Google Fonts remain configured in the page. Review those services and verify that the biography, results, sponsors and contact details are current before a new deployment.
