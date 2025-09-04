---

# QOTD Server

A simple **Quote of the Day (QOTD) server** implemented in Python.
It returns a random quote using `fortune` over TCP/UDP port 17, following [RFC 865](https://www.rfc-editor.org/rfc/rfc865.txt).

---

## Features

* TCP and UDP support on port 17
* Lightweight and suitable for Raspberry Pi or small home servers

---

## Requirements

* Python 3.9+
* `fortune` installed (`sudo apt install fortune`)
* 
---

## Usage

```bash
python qotd_server.py
```

The server listens on TCP and UDP port 17.
Incoming data is ignored, and a random quote is returned.

---

## Example

```
$ nc localhost 17
Circumstances rule men; men do not rule circumstances.
        -- Herodotus
```

```
$ nc -u localhost 17
Debian is like Suse with yast turned off, just better. :)
        -- Goswin Brederlow
```

---

## Security Notes

* UDP is vulnerable to IP spoofing → TCP-only mode recommended for public access
* Consider firewall rules and connection limits for exposed servers

---

## License

MIT License

---
