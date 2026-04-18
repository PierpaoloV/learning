# System Design — URL Shortener (Week 2)

Design a URL shortening service like TinyURL or bit.ly.

## Requirements to address
- Users can submit a long URL and receive a short URL (e.g. `short.ly/abc123`)
- Clicking the short URL redirects to the original URL
- Short URLs should be unique and hard to guess
- System should handle 100M URLs created per day, 10B redirects per day

## Questions to ask yourself before designing
- What is the read/write ratio? (hint: redirects >> creations)
- How long should short URLs live?
- Do we need analytics (click counts)?
- Can two users shorten the same URL to the same short code?

## Write your design in `design.md`
Cover: API design, data model, hashing strategy, DB choice, caching, scaling.
