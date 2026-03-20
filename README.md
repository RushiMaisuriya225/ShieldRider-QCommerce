# ShieldRider-QCommerce
ShieldRider: A dynamic, weekly-premium parametric insurance model securing the livelihoods of gig economy workers against external disruptions.

## The Problem
Q-Commerce delivery partners (Zepto, Blinkit, Swiggy Instamart) are the backbone of our fast-paced economy. But when extreme weather hits—like severe waterlogging—their 10-minute delivery targets become impossible. They get grounded, and they lose 20-30% of their daily earnings. Right now, there is zero safety net for this.

**Our Mission for Phase 1:** Build a safety net strictly for **loss of income** due to these environmental halts. *(Note: We are strictly excluding health, accidents, or vehicle repair coverage, as per the rules!)*

## 💸 The Weekly Premium Model
Gig workers live week-to-week, so a monthly premium makes no sense. We've structured ShieldRider's financial model entirely on a **Weekly pricing basis**. 
We're using Python (Pandas/Scikit-learn) to calculate dynamic weekly premiums based on hyper-local weather risks, ensuring it's affordable for the rider but sustainable for the liquidity pool.

## ⚙️ How It Works (The Core Workflow)
We decided to build a **Native Android App** rather than a web app. Riders are always on their phones, and we need access to native device sensors (more on this below).
1. **Onboarding:** Quick, low-friction setup tailored for gig workers.
2. **Monitoring:** The app pings weather and traffic APIs in the background based on the rider's active zone.
3. **Trigger:** If rainfall exceeds a dangerous threshold (e.g., heavy waterlogging), the parametric trigger fires automatically.
4. **Payout:** Zero-touch processing instantly credits the lost wages for those halted hours.

---

## 🚨 Tackling the "Market Crash" (Anti-Spoofing Strategy)
*Addressing the recent 24-hour threat report regarding GPS-spoofing syndicates.*

We realized that simple GPS verification is useless against organized spoofing. Here is how we are pivoting our architecture to block the syndicate:

* **Sensor Telemetry (Beyond GPS):** Since we are building a native Android app, we can pull data from the accelerometer and gyroscope. A rider fighting through bad weather on a bike has chaotic sensor data. A fraudster spoofing from their bed is completely static. 
* **Network Triangulation:** We aren't just trusting GPS. We are cross-referencing the location with local Cell Tower IDs and nearby Wi-Fi BSSIDs.
* **AI Clustering:** We're using anomaly detection models to spot statistically impossible spikes. If 50 identical claims hit from the exact same geospatial polygon in 2 minutes, the system flags it as a coordinated attack.

### Balancing the UX
We don't want to auto-ban honest riders who just have spotty network coverage in a storm. If a claim is flagged by our anti-spoofing model, we use **Graceful Degradation**. The instant payout pauses, and the app simply asks the rider for a quick liveness check (e.g., "Take a real-time photo of the rain") to verify and release the funds.

## 🛠️ Tech Stack Draft
* **Frontend:** Android (Java/Kotlin) for deep hardware sensor access.
* **Backend:** Python (FastAPI) for handling the logic and API triggers.
* **Data/ML:** NumPy, Pandas, and Scikit-learn for the dynamic weekly pricing and clustering models. We'll drop down to C++ if we hit bottlenecks processing the high-speed sensor data.
