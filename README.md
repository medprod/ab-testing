# A-B Testing 
A/B testing refers to the practice of comparing 2 versions of a variable to see which performs better. The versions (A & B) of a product, where version A remains unchanged 
(as a control variable) and version B we make changes to. We then test if the user is responding better to version A or version B. 

In this program, I calculated the sample size necessary for A/B testing based on statistical hypothesis testing. In order to go further, we must first understand 2 essential
terms:
1. Null Hypothesis = states that there's no different between the control (A) and variant (B) groups
2. Alternate Hypothesis = challenges the null hypothesis by supporting what the researcher believes is true (i.e that there's a difference)

The main objective is always to reject the null hypothesis by collecting the necessary evidence.

## Finding the Sample Size 
To accept/reject the null hypothesis, we need to determine the right sample size of participants for versions A and B. The sample size calculation is dependent on 5 
main parameters:
1. Chosen statistical power
2. Chosen significance level
3. Conversion rate value of out control group (version A)
4. Minimum difference between values of versions A&B conversion rates to be identified
5. One or Two-tailed test

## One/Two Tailed Test
One-Tailed Test: A one-tailed test is used  we want to check the significance of the observed positive difference in variations conversion 
rates (i.e. our goal is to replace variation A with variation B if the latter has better conversion rate).

Two-Tailed test: A two-tailed test is used if we want to check whether conversion rate of A and B differ (i.e. we are interested in both positive and negative difference)

## Example Scneario:
Let's consider a scenario for an online e-commerce platform that wants to conduct an AB test to evaluate the effectiveness of a new website 
layout in improving conversion rates. Here's the scenario:

An e-commerce company has been using a specific website layout for some time but wants to experiment with a new layout to potentially increase conversion rates. 
They plan to conduct an AB test where:

1. Control Group (Group A): Visitors are shown the existing website layout (control) without any changes.
2. Experimental Group (Group B): Visitors are shown the new website layout (experimental) that the company wants to test.
Objective:

The primary objective of the AB test is to determine if the new website layout (experimental group) leads to a statistically significant increase in conversion rates 
compared to the existing layout (control group).

Parameters:

1. Significance Level (Alpha): Typical Value: 0.05 (5% chance of Type I error).
2. Statistical Power (1 - Beta): Typical Value: 0.80 (80% chance of detecting a true effect).
3. Baseline Conversion Rate: Based on historical data or prior knowledge, let's assume a baseline conversion rate of 10% for the existing website layout (control group).
4. Minimum Detectable Effect: The company considers a minimum detectable effect of a 2% increase in conversion rate to be practically significant.
5. Performing both One and Two-Tailed test

## Objective
Control Group Size: To be determined based on the desired statistical power, significance level, baseline conversion rate, and minimum detectable effect.
Experimental Group Size: Typically, the control and experimental groups are of equal size for fairness and comparability in the AB test.
