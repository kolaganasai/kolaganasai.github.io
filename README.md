# Kola Gana Sai · Portfolio

Personal portfolio: SAP ABAP and Python projects, skills, education and contact.

**Live site:** https://kolaganasai.github.io (after you publish it, see below)

Dark navy and saffron design with light and dark mode. As a small extra for SAP recruiters, the "T-code" box in the top bar works like SAP GUI: type a code (or press `/` first) to jump to a section.

| Code | Goes to |
|---|---|
| `ZPROJ` | Projects |
| `ZYOJANA` | Scheme Sahayak |
| `ZSHIELD` | UPI Scam Shield |
| `ZFEE` | College Fee Management & Receipt System |
| `ZSKILL` | Skills |
| `ZEDU` | Education |
| `ZCERT` | Certifications and activities |
| `ZCONTACT` | Contact |

`/n` and `/o` prefixes work too (`/nZPROJ`). Unknown codes show SAP's "Transaction … does not exist" message.

## Projects featured

- **Scheme Sahayak**: multilingual voice assistant for government schemes ([repo](https://github.com/kolaganasai/scheme-sahayak))
- **UPI Scam Shield**: offline scam-SMS detector for Hinglish messages ([repo](https://github.com/kolaganasai/upi-scam-shield))
- **College Fee Management & Receipt System**: SAP ABAP team project ([repo](https://github.com/velpulavinodkumar/college-fee-management-sap-abap))

## Publish on GitHub Pages (free)

1. Create a new public repository on GitHub named exactly **`kolaganasai.github.io`**.
2. Upload everything in this folder (or push it):
   ```bash
   git init
   git add .
   git commit -m "Portfolio"
   git branch -M main
   git remote add origin https://github.com/kolaganasai/kolaganasai.github.io.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
4. After a minute the site is live at **https://kolaganasai.github.io**. Add this link to your resume and LinkedIn.

## Editing

Everything is in `index.html` (plain HTML, CSS and JavaScript, no build step). Images are in `assets/`.

- **Add a project:** copy one `<article class="project">` block, change the text, and give it a `data-tags` value (`python` or `abap`) so the filter works. Add a code for it in the `CODES` list in the script.
- **Update your resumes:** replace `assets/Kola_Gana_Sai_Resume_SAP_ABAP.pdf` or `assets/Kola_Gana_Sai_Resume_Software_AI.pdf` (keep the file names). Note that the PDFs include your phone number and is public once published.
- **Colours and fonts:** change the variables at the top of the `<style>` block. The page supports light and dark mode automatically.

`src/content.html` and `src/build.py` are the source the page was generated from; you can ignore them and edit `index.html` directly.
