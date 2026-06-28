#!/usr/bin/env python3
"""ponytail: one-shot screenshot capture for Coursera submission."""
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8000"
OUT = Path(__file__).resolve().parent / "submission"
OUT.mkdir(exist_ok=True)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})

        page.goto(f"{BASE}/admin/login/")
        page.fill('input[name="username"]', "admin")
        page.fill('input[name="password"]', "admin123")
        page.click('input[type="submit"]')
        page.wait_for_url("**/admin/**")
        page.screenshot(path=str(OUT / "03-admin-site.png"), full_page=True)

        page.goto(f"{BASE}/onlinecourse/login/")
        page.fill('input[name="username"]', "testuser")
        page.fill('input[name="psw"]', "testpass123")
        page.click('button[type="submit"]')
        page.wait_for_url("**/onlinecourse/**")

        page.goto(f"{BASE}/onlinecourse/1/")
        page.click('button[data-target="#exam"]')
        page.check('input[value="1"]')
        page.check('input[value="3"]')
        page.click('input[type="submit"][value="Submit"]')
        page.wait_for_url("**/result/**")
        page.screenshot(path=str(OUT / "07-final.png"), full_page=True)

        browser.close()
        print(f"Saved {OUT / '03-admin-site.png'}")
        print(f"Saved {OUT / '07-final.png'}")


if __name__ == "__main__":
    main()
