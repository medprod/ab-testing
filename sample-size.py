#one-tailed and two-tailed hypothesis testing

from scipy.stats import norm
import math

sig_lvl = 0.05
power = 0.80
cr_control = 0.10
min_diff = 0.02

tail_input = input("Enter 'one' for a one-tailed test or 'two' for a two-tailed test: ")

def zScore(sig_lvl, power, tail_input):
    if tail_input=="one":
        z_score_alpha = norm.ppf(sig_lvl)
        z_score_beta = norm.ppf(1-power)
    
    elif tail_input=="two":
        z_score_alpha = norm.ppf(sig_lvl/2)
        z_score_beta = norm.ppf(1-power)
        
    else:
        raise ValueError("Invalid tail value. Choose 'two' for two-tailed test or 'one' for one-tailed test.")

    return z_score_alpha, z_score_beta

def sampleSize(sig_lvl, power, cr_control, min_diff, tail_input):
    cr_var= cr_control + min_diff
    z_alpha, z_beta = zScore(sig_lvl, power, tail_input)
    n = ((z_alpha+z_beta)**2) * (((cr_control*(1-cr_control)) + (cr_var*(1-cr_var)))) / (min_diff**2)
    
    return n

if tail_input=="one":
    sample_size = sampleSize(sig_lvl, power, cr_control, min_diff, tail_input)
    print("Required sample size per group for a one-tailed test:", sample_size)
    
elif tail_input == "two":
    sample_size = sampleSize(sig_lvl, power, cr_control, min_diff, tail_input)
    print("Required sample size per group for a two-tailed test:", sample_size)
else:
    print("Invalid tail value. Choose 'two' for two-tailed test or 'one' for one-tailed test.")
