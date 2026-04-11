# ForgeTools Business Structure

**Date:** April 1, 2026
**Author:** Dave Liloia
**Status:** Planning document. Not legal advice. Attorney review required before execution.

---

## 1. Entity Structure

### Current State

No formal entity exists. ManagerForge is operating as a sole proprietorship by default, which means Dave is personally liable for everything: Stripe chargebacks, data breaches, contract disputes.

### Recommended Structure: Single-Member LLC

**Option A: Single LLC ("ForgeTools LLC")** (Recommended)
- One LLC holds all products: ManagerForge, GoalForge, HireForge, ProjectForge, The Liloia Method
- Simplest to set up and maintain
- One tax return, one registered agent, one operating agreement
- All products operate as DBAs (doing business as) or just brand names under the LLC
- **Cost:** ~$100 filing + $300/yr registered agent + $0 annual report (if Wyoming/Delaware)
- **Timeline:** 1-2 weeks to form, 2-4 weeks for EIN

**Option B: Series LLC**
- Available in Wyoming, Delaware, Illinois, and a few others
- Each product is a "series" with isolated liability
- Sounds appealing but: most banks don't understand series LLCs, accounting is messy, and courts haven't fully tested the liability shields
- Overkill for a bootstrapped solo founder
- **Not recommended at this stage**

**Option C: Separate LLCs per product**
- Maximum liability isolation
- Maximum administrative burden and cost
- Only makes sense if products have genuinely different risk profiles (e.g., one handles HIPAA data and another doesn't)
- **Not recommended until revenue exceeds $500K+ and products diverge significantly**

### State of Incorporation

**Wyoming** is the best fit for Dave's situation:
- $100 filing fee, $60 annual report
- No state income tax
- Strong privacy protections (no public member disclosure)
- Established LLC case law
- Dave can still operate in any state. If his home state requires foreign LLC registration, he'd file that separately (typically $100-200/yr)

**Delaware** is the other common choice but is more expensive ($300 annual franchise tax minimum) and is optimized for C-corps raising VC, not bootstrapped LLCs.

### Operating Agreement

Even as a single-member LLC, Dave needs a written operating agreement. It should cover:
- Member's capital contribution and ownership (100%)
- Management structure (member-managed)
- Profit distribution policy
- Dissolution procedures
- IP assignment clause: all product IP (code, content, The Liloia Method) is owned by the LLC, not Dave personally
- **Attorney review:** Yes, worth $500-1,000 to have an attorney draft this properly, especially the IP assignment language

### S-Corp Election (Form 2553)

The math: S-corp saves money when self-employment tax on pass-through income exceeds the cost of running payroll. The common threshold is **$50K-80K in net profit**.

- Below $50K net profit: not worth it. Payroll admin costs ($50-100/mo via Gusto or similar) eat the savings.
- At $80K+ net profit: S-corp election typically saves $5K-10K/yr in self-employment taxes
- Can be elected retroactively for the current tax year (before March 15) or prospectively
- **Decision point:** Revisit when ManagerForge MRR hits ~$5K/month consistently

---

## 2. Trademark Strategy

### Priority Order for Federal Trademark Registration

| Priority | Mark | Class | Why |
|----------|------|-------|-----|
| 1 | **ManagerForge** | 42 (SaaS) | Live product, revenue, most brand equity at risk |
| 2 | **ForgeTools** | 42 (SaaS) | Parent brand, needed before launching suite positioning |
| 3 | **The Liloia Method** | 41 (Education/Training) | Book in progress, need to protect before publication |
| 4 | **HireForge** | 42 (SaaS) | File when development starts in earnest |
| 5 | **GoalForge / ProjectForge** | 42 (SaaS) | File when products are near launch |

### Federal Trademark Filing (USPTO)

- **Filing basis:** "Use in commerce" for ManagerForge (it's live). "Intent to use" for products not yet launched.
- **Cost per mark:** $250-350 per class (TEAS Plus or TEAS Standard)
- **Attorney filing:** $500-1,500 per mark on top of USPTO fees. Recommended for the first filing; you can self-file subsequent ones using the same format.
- **Timeline:** 8-12 months from filing to registration if no opposition
- **Total for top 3 marks:** ~$2,500-4,500 (USPTO fees + attorney for first filing)

### Common Law Protection (Immediate, Free)

Before federal registration, Dave already has common law trademark rights by using these names in commerce. To strengthen that position:
- Use the TM symbol (not the registered R symbol) on all product names now
- Document first use dates for each mark
- Keep records of marketing materials, screenshots, and customer communications using each name
- This provides regional protection but is weaker than federal registration

### Domain Strategy

**Secure immediately (before anyone else does):**
- forgetools.com (check availability, likely available or purchasable)
- hireforge.com
- goalforge.com
- projectforge.com
- thelilioamethod.com
- lilioamethod.com

**Already secured (assumed):**
- managerforge.com

**Cost:** ~$10-15/domain/year. Total for 6 domains: ~$70-90/year. Cheap insurance.

**Action:** Register all through one registrar (Namecheap, Cloudflare, or Google Domains) with auto-renew and WHOIS privacy enabled.

---

## 3. Legal Documents Needed

### Current State: Critical Gap

The Terms of Service page at managerforge.com/terms says "coming soon." The Privacy Policy page has principles listed but is not a complete legal document. **This is a real risk.** Dave is processing user data, taking payments, and using AI on potentially sensitive employee performance information with no enforceable terms.

### What Needs to Happen Before Anything Else

**Priority 1: ManagerForge Terms of Service**
Must cover:
- Acceptable use policy (no discriminatory use of AI outputs, etc.)
- AI disclaimer: outputs are suggestions, not legal/HR advice
- Data ownership: users own their data, Dave owns the platform and AI models
- Limitation of liability (critical for AI-generated content about employees)
- Subscription terms, cancellation, refund policy (the 30-day guarantee mentioned on pricing)
- DMCA/IP provisions
- Governing law and dispute resolution
- **Attorney review:** Required. An AI/SaaS attorney should draft this. Budget $1,500-3,000.

**Priority 2: ManagerForge Privacy Policy**
Must cover:
- What data is collected (meeting notes, audio, employee names, AI-generated insights)
- How AI processes data (Claude API, what's sent, what's retained)
- Anthropic's data processing terms (confirm Claude API doesn't train on input)
- Third-party processors: Stripe, Vercel, DigitalOcean, AWS S3, Resend, Sanity, Deepgram
- Data retention and deletion procedures
- Cookie policy
- CCPA compliance (California users)
- GDPR basics if any EU users exist
- **Attorney review:** Required. Same attorney can do both ToS and Privacy. Bundle pricing likely $2,500-4,000 total.

### Suite-Wide vs. Per-Product Legal Docs

**Recommended approach:** One set of legal documents for "ForgeTools" that covers all products, with product-specific appendices as needed.

- The ToS references "ForgeTools services, including ManagerForge, HireForge, and other products"
- Each product page links to the same ToS and Privacy Policy
- Product-specific data processing details go in appendices
- This avoids maintaining 4+ sets of legal docs

### Before Launching the Next Product

Checklist:
- [ ] ForgeTools LLC formed
- [ ] ToS and Privacy Policy live and legally reviewed
- [ ] IP assignment from Dave personally to the LLC
- [ ] Stripe account updated to LLC entity
- [ ] Data Processing Addendum (DPA) template ready for enterprise customers who request one
- [ ] Cookie consent banner (if not already implemented)

### Data Processing Considerations

Dave's "privacy-first" positioning is a genuine competitive advantage in the HR-adjacent space. To back it up:
- Confirm in writing (via Anthropic's terms) that Claude API does not train on user inputs
- Document all sub-processors and their data handling
- Implement data export and deletion features (GDPR "right to be forgotten")
- Consider SOC 2 Type I certification when revenue supports it ($10K-30K). Not needed now, but enterprise customers will ask.

---

## 4. Multi-Product Website Strategy

### Option A: forgetools.com as Hub Site

A dedicated marketing site at forgetools.com that presents the suite, with each product having its own subdomain or domain.

**Structure:**
- forgetools.com: suite overview, The Liloia Method, about Dave, pricing comparison
- managerforge.com: product site + app (current)
- hireforge.com: product site + app (future)

**Pros:**
- Clean brand architecture
- Each product has its own SEO identity
- Tells a "platform" story to investors or acquirers

**Cons:**
- Another site to build and maintain
- Premature when only one product exists
- Splits SEO authority across domains
- Costs time that should go toward product development

### Option B: ForgeTools Section on managerforge.com

Add a /forgetools or /suite page to the existing ManagerForge site. Light touch.

**Structure:**
- managerforge.com/suite: "Part of the ForgeTools suite" page
- managerforge.com remains the primary site
- Future products get their own domains when they launch

**Pros:**
- Zero additional infrastructure
- Concentrates all SEO authority on one domain
- Can be built in a day
- Natural evolution: ManagerForge is the flagship, other products are "coming soon"

**Cons:**
- ManagerForge site doing double duty can feel cluttered
- Harder to differentiate product brands later

### Option C: Minimal Approach (Recommended)

No separate ForgeTools site. Just consistent branding across products.

**Structure:**
- managerforge.com stays as-is
- Footer reads: "ManagerForge is a ForgeTools product"
- forgetools.com domain is registered but redirects to managerforge.com (or parks with a simple "ForgeTools: Tools for Modern Managers" page)
- When product #2 launches, reassess

**Pros:**
- Zero distraction from building and selling ManagerForge
- Domains are secured (defensive)
- No premature "suite" positioning that could confuse a market that doesn't know you yet
- Revisiting is easy; there's no sunk cost

**Cons:**
- Less impressive if Dave is pitching the "platform vision" to potential partners or press
- Slightly more work to retrofit later

### Recommendation

**Go with Option C now. Revisit when product #2 is 30 days from launch.**

The minimum viable suite presence is:
1. Register forgetools.com
2. Add "A ForgeTools product" to the ManagerForge footer
3. Park forgetools.com with a one-page "coming soon" or redirect
4. That's it

Dave's time is better spent getting ManagerForge to 25 paying customers than building a suite website for products that don't exist yet.

---

## 5. Pricing Architecture

### Current ManagerForge Tiers

| Tier | Price | Target |
|------|-------|--------|
| Free | $0/mo | Trial, individual managers exploring |
| Starter | $19/mo | Individual managers, basic needs |
| Professional | $39/mo | Active managers, full AI features |
| Team | $99/mo | Managers wanting premium features |

### How Additional Products Fit: Three Models

**Model 1: Independent Pricing (Recommended for Now)**

Each product has its own pricing tiers. Cross-product discounts available.
- ManagerForge: $0/19/39/99
- HireForge: $0/19/39 (for example)
- Bundle discount: 20% off total when subscribing to 2+ products

**Why this works now:**
- Products serve different jobs (ongoing 1:1s vs. episodic hiring)
- Users may want one product but not others
- Simplest to implement in Stripe
- Each product proves its own value proposition

**Model 2: Unified Platform Tier**

One subscription, all products included.
- ForgeTools Free: limited access to all products
- ForgeTools Pro: $49/mo, full access to all products
- ForgeTools Team: $99/mo, everything + team features

**Risk:** Bundling unproven products with a proven one can suppress revenue if people would have paid full price for ManagerForge alone. Also creates pressure to keep all products at the same quality level.

**When this makes sense:** When 3+ products are live and there's data showing users want multiple products.

**Model 3: Platform + Add-ons**

Base platform subscription + per-product add-ons.
- ForgeTools Base: $29/mo (includes one product of choice)
- Additional products: +$15/mo each
- All-access: $59/mo

**Complexity warning:** This creates a pricing matrix that's hard to communicate on a landing page. Not recommended until the product catalog is large enough to justify it.

### Cross-Product Upsell Strategy

The natural upsell path follows the manager lifecycle:
1. Manager discovers ManagerForge (1:1 tool)
2. When they need to hire, surface HireForge
3. After hiring, surface OnboardForge (if built)
4. The Liloia Method content cross-sells across all products

**Implementation (decide later, but architect now):**
- Shared user accounts across products (same auth system)
- In-app prompts: "Hiring someone new? Try HireForge" when a user adds a new team member
- Email sequences triggered by product usage patterns
- Unified billing dashboard

### What to Decide Now vs. Later

**Decide now:**
- Shared authentication strategy (NextAuth config that works across products)
- Stripe account structure (one Stripe account, products as separate Stripe Products)
- User data model that supports multi-product (a `products` or `subscriptions` table, not hardcoded to ManagerForge)

**Decide later:**
- Bundle pricing specifics
- Cross-product discount amounts
- Whether to unify into platform tiers
- Enterprise/team pricing across the suite

---

## 6. Immediate Action Items

### Next 30 Days (April 2026)

**Legally necessary:**
1. [ ] **Form Wyoming LLC** ("ForgeTools LLC"). Use a registered agent service like Northwest ($125/yr) or Wyoming Agents ($50/yr). File online at Wyoming Secretary of State. ~$100 + agent fee.
2. [ ] **Get EIN** from IRS (free, online, instant if done during business hours).
3. [ ] **Open a business bank account.** Separate personal and business finances immediately. Mercury or Relay are good options for solo founders. Free.
4. [ ] **Update Stripe** to the LLC entity once formed. This is important for liability protection.
5. [ ] **Hire an attorney** to draft Terms of Service and Privacy Policy. Budget $2,500-4,000. Ask for SaaS/AI experience specifically. Referral sources: local bar association, LegalZoom's attorney network, or recommendations from other SaaS founders.

**High value, low effort:**
6. [ ] **Register domains:** forgetools.com, hireforge.com, goalforge.com, projectforge.com, thelilioamethod.com, lilioamethod.com. ~$70-90 total.
7. [ ] **Add TM symbol** to ManagerForge branding on the live site (header, footer, pricing page).
8. [ ] **File trademark application** for "ManagerForge" (Class 42, use in commerce basis). $250-350 USPTO + optional attorney assist.
9. [ ] **Add "A ForgeTools product" to ManagerForge footer.** 5-minute code change.

### Before Product #2 Launches

- [ ] ToS and Privacy Policy live and reviewed by attorney
- [ ] IP formally assigned to the LLC (attorney can include this in operating agreement)
- [ ] ForgeTools trademark filed
- [ ] The Liloia Method trademark filed (before book goes public)
- [ ] Shared auth architecture designed (even if not built yet)
- [ ] Stripe multi-product structure set up
- [ ] DPA template ready for enterprise requests
- [ ] Cookie consent banner implemented

### Nice-to-Have (Not Blocking)

- Series LLC or additional entities: not needed until products have materially different risk profiles
- S-corp election: revisit when net profit exceeds $50K/yr
- SOC 2 certification: revisit when enterprise customers are requesting it
- forgetools.com marketing site: revisit when product #2 is 30 days from launch
- Unified platform pricing: revisit when 2+ products are live with paying users

---

## Cost Summary

| Item | Cost | Timeline |
|------|------|----------|
| Wyoming LLC formation | ~$160 (filing + agent) | 1-2 weeks |
| EIN | Free | Same day |
| Business bank account | Free | 1 week |
| Domain registrations (6) | ~$80/yr | Same day |
| ManagerForge trademark | ~$350-850 (with attorney) | 8-12 months to register |
| Attorney: ToS + Privacy Policy | ~$2,500-4,000 | 2-4 weeks |
| Attorney: Operating Agreement | ~$500-1,000 | 1-2 weeks |
| **Total immediate investment** | **~$3,600-6,100** | |

This is the cost of legitimizing the business. None of it is optional if Dave is taking money from customers and processing their employee data through AI.

---

*This document should be reviewed with a business attorney before acting on any legal recommendations. State-specific requirements (business registration, tax obligations) depend on Dave's state of residence.*
