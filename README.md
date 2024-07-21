# SVOR
SVOR analysis in the command line!

## What is SVOR Analysis?
In short, a modification of SWOT that allows for mathematically-correct decision-making.

## "I'm a business guy! How haven't I heard about this?"
It was featured on three webpages, all of which use the same book as a source. It seems to have been created by Olivier Mesly, though his book only briefly touches on it. I decided to figure out the analysis algorithm myself.

## EXPLAIN!
First, one gathers the Strengths/Vulnerabilities/Opportunities/Risks of a situation, and also notes the Infrastructure. A constant "k" is also determined.

<table>
<tr>
<td width="25%"">
S
</td>
<td width="25%">
O
</td>
</tr>
<tr>
<td width="25%">
V
</td>
<td width="25%">
R
</td>
<td width="25%">
I
</td>
<td width="25%">
k
</td>
</tr>
</table>

Specific points may be given to each item to adjust its importance, but the default weight is 1.

Next, you determine relational strategies between internal and external elements.

- Strengths are internal and positive.
- Opportunities are external and positive.
- Vulnerabilities are internal and negative.
- Risks are external and negative.

**Strength** -> **Opportunity**
Use strengths to take advantage of opportunities.

**Vulnerabilities** -> **Opportunity**
Overcome vulnerabilities by taking advantage of opportunities.

**Risk** -> **Strength**
Use strengths to avoid risks.

**Risk** -> **Vulnerability**
Minimize vulnerabilities and avoid risks.

We then create a chart of absolute positive, absolute mathematical, and absolute negative forces (and their lesser absolutes):

| FORCE |	INTERNAL | MATHEMATICAL	| EXTERNAL |
| --- | --- | --- | --- |
| +	| Total Forces | I / O = TFgC | Opportunities |
| MATH | 1 / TF = VgC | k	| 1 / R = OgC |
| -	|	Vulnerabilities	| k / V = RgC	|	Risks |

**Total Forces** are the total of all elements, including **Infrastructure** & strategies.
**Infrastructure** divided by **Opportunities** gives us our **Total Forces Given Constraints**.
**Opportunities** are opportunities.
1 divided by our **Total Forces** gives us our **Vulnerabilities Given Constraints**.
Our **constant "_k_"** can be adjusted depending on the working averages of similar situations of the past.
1 divided by our **Risks** gives us our **Opportunities Given Constraints**.
**Vulnerabilities** are vulnerabilities.
***k*** divided by **Vulnerabilities** gives us our **Risks Given Constraints**.
**Risks** are risks.

We now separate our *absolute positive* and *absolute negative* values, ignoring **Total Forces**. 

| + | - |
| --- | --- |
| TFgC | Vulnerabilities |
| O | RgC |
| OgC | Risks |
| | VgC |

We then divide our positive values by our negative values, leaving us with our **adjusted SVOR value**. If it's positive, it's more likely that the decision should be made. If negative, it's best to re-consider.

Things to consider:
- The constant "k" is completely arbitrary and based on previous instances with pre-calculated values. One can review past cases with adjusted k constants to get a more fair means for future k values.
- Considering all totally-positive forces while ignoring VgC and OgC will always result in a positive bias, so long as Strengths & Opportunities only have positive weighted value points.
- Two different SVOR values can be considered in analysis: Absolute, and Modified. Absolute treats Total Forces as a positive value used in final totals, and ignores VgC & OgC. Modified ignores Total Forces as a value, and considers OgC positive and VgC negative.
- Final SVOR values only mean anything when compared to previously-analyzed values of similar situations. The more of the same situation analyzed, the more accurate the readout can be.

## What are the elements exactly?

Extremely similar to SWOT! A lot of it is actually carried over:

**Strengths**: Characteristics that give a decision an advantage over others.
**Vulnerabilities**: Characteristics that give a decision a disadvantage relative to others.
**Opportunities**: External factors that can be exploited to the advantage of the overall decision.
**Risks**: External factors that can cause trouble for the overall decision.
**Infrastructure**: All environmental objects, both actual and abstract.

***Infrastructure*** can be a bit confusing, but it's essentially anything that can be a remote factor directly to the other elements. For instance, if the decision is to change the oil of your car:
- The car.
- The oil.
- The oil-changing equipment.
- The weather.
- The environment in which the oil is changed.

The more specific one chooses to get with the infrastructure, the more of a weight the **Infrastructure** element has. One may adjust weights accordingly.
