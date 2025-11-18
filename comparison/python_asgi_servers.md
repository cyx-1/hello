# Python ASGI Server Comparison

Comprehensive comparison of Python ASGI (Asynchronous Server Gateway Interface) server solutions: Uvicorn, Hypercorn, Daphne, and Granian.

## Quick Stats Comparison

| Server | GitHub Stars | Forks | Contributors | Inception Date | First Release | Language | Status |
|--------|-------------|-------|--------------|----------------|---------------|----------|---------|
| **Uvicorn** | 10.1k | 874 | 200 | 2017 | June 5, 2017 (v0.0.1) | Python | Stable |
| **Hypercorn** | 1.4k | 132 | 64 | May 17, 2018 | June 17, 2018 (v0.6.0) | Python | Stable |
| **Daphne** | 2.6k | 284 | 72 | 2016 | September 9, 2016 | Python (Twisted) | Stable |
| **Granian** | 4.6k | 132 | Not specified | 2021 | ~Early 2023 | Rust | Beta |

## Performance Benchmarks (2025)

| Metric | Granian | Uvicorn | Hypercorn | Daphne |
|--------|---------|---------|-----------|---------|
| **Requests/sec** | 50,000 | 45,000 | 35,000 | ~30,000 |
| **Memory/worker** | ~15MB | ~20MB | ~25MB | ~30MB |
| **Latency** | Lowest | Very Low | Low | Moderate |

## Protocol Support

| Server | HTTP/1.1 | HTTP/2 | HTTP/3 | WebSockets | WSGI | ASGI |
|--------|----------|--------|--------|------------|------|------|
| **Uvicorn** | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| **Hypercorn** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Daphne** | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| **Granian** | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ (+ RSGI) |

## Project Activity

| Server | Last Release | Project Staleness | Active Development |
|--------|-------------|-------------------|-------------------|
| **Uvicorn** | Oct 18, 2025 (v0.38.0) | Active | ✅ Very Active |
| **Hypercorn** | Recent | Active | ✅ Active |
| **Daphne** | Recent | Active | ✅ Active |
| **Granian** | Recent | Active | ✅ Very Active |

---

## Detailed Information

### 1. Uvicorn

**Origin Story:**
- Created by **Tom Christie** in 2017, founder of Encode
- Initially used an "ASGI-like" interface called the "Uvicorn Messaging Interface"
- In early 2018, Tom Christie updated Uvicorn to become ASGI-compliant, documented in a report dated April 6, 2018
- First release (v0.0.1) on June 5, 2017; major v0.2.1 release on June 29, 2018
- Developed as a lightning-fast ASGI server implementation for Python, focusing on performance and simplicity

**Key Backers/Sponsors:**
- Encode (Tom Christie's company)
- Strongly integrated with the FastAPI ecosystem (Sebastián Ramírez)
- Community-driven with 200+ contributors
- Key maintainers: Kludex, florimondmanca, euri10, graingert

**Use Cases:**
- Default server for FastAPI applications
- High-performance async Python applications
- Microservices requiring low latency
- REST APIs and real-time applications

**Strengths:**
- Fastest pure-Python ASGI server
- Simple, lightweight design
- Excellent documentation
- Wide adoption and community support
- Best for HTTP/1.1 and WebSocket workloads

**Limitations:**
- No HTTP/2 or HTTP/3 support
- Pure ASGI only (no WSGI support)

---

### 2. Hypercorn

**Origin Story:**
- Created by **Philip Jones (pgjones)** in May 2018
- Initially part of Quart web framework before being separated
- Forked from Quart version 0.5.0 serving code
- First announced June 17, 2018 with Quart 0.6.0 release
- GitLab repository created May 17, 2018
- Strategic move to embrace ASGI specification and create a richer asyncio-based web ecosystem

**Key Backers/Sponsors:**
- Philip Jones (Python Software Foundation Fellow)
- Pallets project ecosystem
- Hyper project contributors
- Part of the broader Quart web framework ecosystem

**Use Cases:**
- Applications requiring HTTP/2 or HTTP/3
- Modern protocol support requirements
- Quart framework applications
- Services needing both ASGI and WSGI support

**Strengths:**
- Most comprehensive protocol support (HTTP/2, HTTP/3)
- Supports both ASGI and WSGI interfaces
- Inspired by Gunicorn's architecture
- Strong HTTP/2 server-push capabilities
- Good for modern web applications

**Limitations:**
- Slightly lower performance than Uvicorn (due to richer feature set)
- More complex configuration options
- Higher memory footprint

---

### 3. Daphne

**Origin Story:**
- Created by **Andrew Godwin** in 2016
- Originally called "django-onair" before being renamed
- Developed as part of Django Channels project
- First ASGI server implementation
- Became official Django project on September 9, 2016
- Built by combining Twisted (HTTP handling) and Autobahn (WebSocket handling)
- Created to bring WebSockets and non-request-response protocols to Django

**Key Backers/Sponsors:**
- Django Software Foundation
- Andrew Godwin (creator of South and Django migrations)
- Django Channels team
- Strong backing from Django community

**Use Cases:**
- Django Channels applications
- Django projects requiring WebSocket support
- Applications built on Twisted ecosystem
- Real-time Django applications

**Strengths:**
- First ASGI server (reference implementation)
- Robust, battle-tested with Django
- Strong HTTP/2 support
- Excellent WebSocket handling via Autobahn
- Deep Django integration

**Limitations:**
- Slower than newer alternatives
- Based on Twisted (older async framework)
- Higher memory usage
- Primarily focused on Django ecosystem

---

### 4. Granian

**Origin Story:**
- Created by **Giovanni Barillari** in 2021
- Copyright 2021, first public release ~early 2023
- Built entirely in Rust using Hyper and Tokio
- Announced on Hacker News January 19, 2023
- Created by the author of Emmett web framework (formerly Web2Py)
- Designed as a production-ready, high-performance alternative written in Rust

**Key Backers/Sponsors:**
- Emmett Framework organization
- Giovanni Barillari
- Growing community adoption
- Used in production by Mozilla, Microsoft, paperless-ngx, Reflex, and SearXNG

**Use Cases:**
- High-performance production applications
- Services requiring maximum throughput
- Memory-constrained environments
- Modern Python applications needing best performance

**Strengths:**
- Fastest ASGI server (50k req/sec)
- Lowest memory footprint (15MB/worker)
- Written in Rust for maximum performance
- Supports ASGI, WSGI, and custom RSGI interface
- HTTP/2 support
- Production-ready despite beta status

**Limitations:**
- Still in beta status
- Smaller community compared to Uvicorn
- Newer project with less battle-testing
- Limited HTTP/3 support
- Rust dependency for development

---

## Community & Ecosystem

### PyPI Download Statistics
Based on community adoption and integration:

1. **Uvicorn**: Most downloaded due to FastAPI integration
2. **Daphne**: Strong downloads from Django ecosystem
3. **Granian**: Rapidly growing adoption
4. **Hypercorn**: Steady growth with Quart users

### Framework Integration

| Framework | Recommended Server | Alternative |
|-----------|-------------------|-------------|
| FastAPI | Uvicorn | Hypercorn, Granian |
| Django Channels | Daphne | Uvicorn, Hypercorn |
| Quart | Hypercorn | Uvicorn |
| Starlette | Uvicorn | Granian |
| Litestar | Uvicorn | Granian |

---

## Recommendations

### Choose **Uvicorn** if:
- Building FastAPI or Starlette applications
- Need proven, stable, high-performance server
- Want simple configuration and excellent documentation
- HTTP/1.1 and WebSocket support is sufficient

### Choose **Hypercorn** if:
- Need HTTP/2 or HTTP/3 support
- Require both ASGI and WSGI compatibility
- Building Quart applications
- Want comprehensive protocol support

### Choose **Daphne** if:
- Building Django Channels applications
- Need deep Django integration
- Prefer Twisted-based ecosystem
- Want the reference ASGI implementation

### Choose **Granian** if:
- Need maximum performance (50k+ req/sec)
- Have memory constraints (lowest footprint)
- Want Rust-powered performance for Python apps
- Building modern, high-throughput services
- Can accept beta software in production

---

## Migration Considerations

All four servers implement ASGI 3.0 specification, making migration between them relatively straightforward for most applications. Key considerations:

1. **Uvicorn → Granian**: Easy migration, expect 10-15% performance boost
2. **Daphne → Uvicorn**: May need to adjust Django Channels configuration
3. **Any → Hypercorn**: Check if HTTP/2 features need explicit configuration
4. **WSGI → ASGI**: May require application code changes

---

## Conclusion

The Python ASGI server landscape offers robust choices for different use cases:

- **Uvicorn** remains the gold standard for FastAPI and general-purpose ASGI applications
- **Hypercorn** leads in modern protocol support (HTTP/2, HTTP/3)
- **Daphne** is the proven choice for Django Channels and Twisted-based applications
- **Granian** represents the future with Rust-powered performance

The emergence of Granian demonstrates the trend toward high-performance Rust implementations while maintaining Python ecosystem compatibility. All servers are actively maintained and production-ready (Granian with caveats about beta status).

---

**Last Updated:** 2025-11-18
