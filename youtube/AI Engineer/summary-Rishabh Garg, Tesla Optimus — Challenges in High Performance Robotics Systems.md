# Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems

**Video URL:** https://www.youtube.com/watch?v=bCGbuyv8PMk

---

## Executive Summary

Rishabh Garg from Tesla Optimus delivers a technical deep dive into the critical software infrastructure challenges in building high-performance robotics systems. The talk focuses on what happens "between the controller and the wire" - the often-overlooked software systems that connect robot policies to actuators. Through building a toy robotics system, Garg systematically reveals common performance bottlenecks including CAN bus saturation, threading issues, scheduling problems, memory contention, and interrupt handling. He demonstrates how issues that appear to be policy failures are often actually software system problems, providing practical debugging techniques and solutions for each challenge.

---

## Topics

### [Introduction: The Software-Hardware Gap](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=17s)
- The challenge of diagnosing robot failures: is it the policy or the software system?
- Focus on the infrastructure between controllers and actuators
- Building a toy robotics architecture to explore common issues

**Key Points:**
- Robots have complex systems with many software components
- When motors don't move as expected, root cause could be in multiple places
- Many issues look like policy problems but are actually software infrastructure issues

### [System Architecture & CAN Bus Basics](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=83s)
- Basic robot architecture: actuators, CPU, accelerator, sensors
- CAN protocol choice: open source, affordable, sufficient data rate
- Simple control loop: receive data → policy → send data

**Key Points:**
- CAN bus is widely compatible but has bandwidth limitations
- Initial assumption: 2ms policy execution time
- Simple sequential loop design as starting point

### [Problem 1: CAN Bus Bandwidth Saturation](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=145s)
- Expected 2ms loop time, but observing gaps in execution
- CAN bus math: 10 messages × 100 bits = 1000 bits at 1 Mbps = 1ms transmission time
- Transmission time comparable to loop time creates bottleneck

**Key Points:**
- Even small message counts can saturate CAN bus
- 1ms gap appears due to communication overhead
- Communication bandwidth becomes a first-order concern

### [Solution 1: Multithreading & Pipelining](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=201s)
- Breaking loop into components: TX, RX, and Policy
- Running communication in separate thread from policy
- Pipelining approach: overlap RX for next iteration with current TX

**Key Points:**
- Parallel RX and TX execution while maintaining policy timing
- Data received for next iteration while transmitting previous results
- Achieves 2ms effective loop time despite 1ms communication overhead

### [Problem 2: Message Jitter & Timing Irregularities](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=277s)
- New symptom: actuators stuttering, making catching-up sounds
- Using external CAN transceiver to capture bus timing data
- Cycle time plots reveal messages arriving irregularly (0ms, then 4ms gaps)

**Key Points:**
- Messages queuing instead of sending on time
- Some messages arrive together, others are delayed
- Appears as mechanical issues but is software timing problem

### [Root Cause: Policy Timing Variability](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=422s)
- Policies are not deterministic in execution time
- When policy runs long, message misses send window and queues
- Next iteration sends both queued and current messages together

**Key Points:**
- TX/RX threads can desynchronize
- Queued messages create irregular timing patterns
- Need better scheduling to maintain consistent timing

### [Problem 3: Scheduling & Thread Priority](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=460s)
- Operating system scheduler doesn't prioritize robot control threads
- Linux scheduler treats all processes equally without context
- CPU utilization shows thread 2 (comms) not running when needed

**Key Points:**
- Default OS scheduling insufficient for real-time requirements
- Threads can be pre-empted at critical moments
- Need explicit thread priority and scheduling policies

### [Solution 2: Real-Time Scheduling (SCHED_FIFO)](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=566s)
- Using SCHED_FIFO for communication thread priority
- Priority levels: kernel interrupts (0-49), user real-time (50-99), normal (100)
- Setting communication thread to priority 99 for highest user-space priority

**Key Points:**
- SCHED_FIFO ensures thread runs to completion without pre-emption
- Communication thread gets CPU immediately when data arrives
- Must be careful not to starve other critical threads

### [Problem 4: Memory Allocation & Page Faults](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=688s)
- Memory access causing delays even with proper scheduling
- Virtual memory and page faults introduce latency
- Memory might be swapped to disk, requiring retrieval

**Key Points:**
- Operating system manages memory in pages (4KB chunks)
- Page faults can add milliseconds of delay
- Virtual memory abstraction creates unpredictability

### [Solution 3: Memory Locking (mlock/mlockall)](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=761s)
- Using mlock to lock critical memory pages in RAM
- mlockall to lock all process memory
- Prevents swapping and eliminates page fault delays

**Key Points:**
- Memory locking ensures immediate access
- Trade-off: reduces available memory for other processes
- Critical for real-time performance

### [Problem 5: CPU Cache Misses](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=820s)
- L1/L2/L3 cache hierarchy and latency differences
- Cache miss requires RAM access (100x slower than L1)
- Data locality and prefetching matter for performance

**Key Points:**
- L1 cache: ~1ns, L2: ~10ns, L3: ~40ns, RAM: ~100ns
- Cache line size (64 bytes) affects access patterns
- Memory layout impacts performance significantly

### [Solution 4: Cache Optimization Strategies](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=887s)
- Aligning data structures to cache line boundaries
- Batching operations to maximize cache hits
- Understanding prefetching behavior

**Key Points:**
- Align data to 64-byte boundaries
- Group related data together
- Sequential access patterns perform better

### [Problem 6: Interrupt Handling Delays](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=946s)
- CAN controller interrupts can be delayed by other interrupt handlers
- Interrupt priorities and sharing issues
- Interrupt coalescing can batch notifications

**Key Points:**
- Hardware interrupts compete for CPU time
- Multiple devices sharing interrupt lines
- Interrupt handling adds variable latency

### [Solution 5: Interrupt Optimization](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=1012s)
- Setting interrupt priorities (similar to thread priorities)
- Using dedicated interrupt lines when possible
- Configuring interrupt coalescing parameters

**Key Points:**
- Prioritize robot control interrupts
- Minimize interrupt sharing
- Tune coalescing for latency vs throughput trade-off

### [Advanced Topic: Kernel Bypass Techniques](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=1078s)
- Bypassing kernel for direct hardware access
- User-space drivers and polling approaches
- Trade-offs between latency and CPU utilization

**Key Points:**
- Kernel bypass eliminates context switching overhead
- Requires dedicated CPU cores (polling)
- Appropriate for ultra-low-latency requirements

### [Debugging Methodology](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=310s)
- Using external CAN transceivers to capture bus data
- Tools like candump for timestamped message capture
- Cycle time plots to visualize timing issues

**Key Points:**
- External monitoring provides ground truth
- Timestamp analysis reveals patterns
- Visualization helps identify root causes

### [Practical Recommendations & Takeaways](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=1144s)
- Systematic approach to diagnosing robot performance issues
- Understanding the full stack from policy to hardware
- Balancing performance optimizations with system complexity

**Key Points:**
- Don't assume issues are in the policy - investigate the full stack
- Use real-time OS features appropriately
- Profile and measure before optimizing
- Consider trade-offs of each optimization technique

### [Q&A Highlights](https://www.youtube.com/watch?v=bCGbuyv8PMk&t=1200s)
- Discussion of CAN-FD and higher bandwidth protocols
- Tesla's specific approach to these challenges
- Future directions in robotics systems

**Key Points:**
- Protocol selection depends on bandwidth and latency requirements
- Some problems require hardware changes, not just software
- Continuous evolution of best practices in robotics systems

---

## Key Technical Concepts

**CAN Bus Limitations:**
- 1 Mbps standard bandwidth
- ~100 bits per message typical overhead
- Becomes bottleneck with 10+ messages per cycle

**Real-Time Linux Features:**
- SCHED_FIFO: First-in-first-out real-time scheduling
- Priority range: 0-99 (higher = more priority)
- Memory locking: mlock, mlockall
- CPU affinity and isolation

**Performance Hierarchy:**
- L1 Cache: ~1ns access time
- L2 Cache: ~10ns access time
- L3 Cache: ~40ns access time
- RAM: ~100ns access time
- Page fault: milliseconds

**Threading Model:**
- Separate threads for TX, RX, and Policy
- Pipelined execution to overlap I/O and computation
- Careful synchronization to avoid data races

---

## Lessons Learned

1. **Infrastructure Matters**: High-performance robotics requires careful attention to the software infrastructure, not just the ML policy
2. **Measure First**: Use external tools to capture ground truth before assuming root cause
3. **Systematic Debugging**: Work through the stack methodically - communication, scheduling, memory, cache, interrupts
4. **Real-Time is Hard**: Achieving consistent low-latency performance requires using OS real-time features properly
5. **Trade-offs Everywhere**: Each optimization (priority, memory locking, kernel bypass) has costs in terms of system resources or complexity

---

*This summary was created from the video transcript and organized by topic with clickable timestamps for easy navigation.*
