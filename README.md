# ShieldRider-QCommerce
ShieldRider: A dynamic, weekly-premium parametric insurance model securing the livelihoods of gig economy workers against external disruptions.

## The Problem
Q-Commerce delivery partners (Zepto, Blinkit, Swiggy Instamart) are the backbone of our fast-paced digital economy. But when extreme weather hits—like severe waterlogging—their 10-minute delivery targets become impossible. They get grounded, and they lose 20-30% of their daily earnings. Right now, gig workers have no income protection against these uncontrollable events.

**Our Mission for Phase 1:** Build a safety net strictly for **loss of income** due to these environmental halts. *(Note: We are strictly excluding health, accidents, or vehicle repair coverage, as per the rules!)*

## The Weekly Premium Model
Gig workers operate week-to-week. We've structured ShieldRider's financial model entirely on a **Weekly pricing basis**. 
We're using Python (Pandas/Scikit-learn) to calculate dynamic weekly premiums based on hyper-local weather risks, ensuring it's affordable for the rider but sustainable for the liquidity pool.

## How It Works (The Core Workflow)
We decided to build a **Native Android App** rather than a web app. Riders are always on their phones, and native camera integration is essential for our new verification flow.
1. **Onboarding:** Quick, low-friction setup optimized for our delivery persona.
2. **Monitoring:** The app pings weather APIs and traffic data in the background based on the rider's active zone.
3. **Trigger:** If rainfall exceeds a dangerous threshold (e.g., heavy waterlogging), the parametric trigger fires automatically.
4. **Payout:** Zero-touch processing instantly credits the lost wages for those halted hours.

---

## Tackling the "Market Crash" (Anti-Spoofing Strategy)
*Addressing the recent 24-hour threat report regarding GPS-spoofing syndicates.* 

We realized that simple GPS verification is officially obsolete against organized spoofing. Here is how we pivoted our architecture to block the syndicate without over-engineering:

* **AI Clustering (Anomaly Detection):** To differentiate between a genuinely stranded delivery partner and a bad actor spoofing their location, our system utilizes anomaly detection. If the ML model detects a statistically impossible spike of identical claims originating from the exact same geospatial polygon within a 2-minute window, it flags the event as a coordinated syndicate attack.
* **Contextual Photo Check (Beyond Basic GPS):** We needed data points beyond basic GPS coordinates to detect a coordinated fraud ring. Instead of relying purely on easily manipulated location data, flagged claims trigger a real-world liveness check. 

### Balancing the UX
We must handle flagged claims without unfairly penalizing honest gig workers who might just be experiencing a genuine network drop in bad weather. When our AI clustering model flags a claim, we use **Graceful Degradation**. The instant payout pauses, and the app simply asks the rider to snap a quick, live photo of the weather conditions to verify and release the funds. A real rider can do it in two seconds; a scammer sitting at home cannot.

## Tech Stack Draft
* **Frontend:** Android (Java/Kotlin) for camera integration and UI.
* **Backend:** Python (FastAPI) for handling the core business logic, API triggers, and image verification workflows.
* **Data/ML:** NumPy, Pandas, and Scikit-learn for building the predictive risk modeling, dynamic weekly pricing, and anomaly detection clustering models.
