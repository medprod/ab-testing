#Checking for statistical significance
from scipy.stats import norm
import math

sig_lvl = 0.05
power = 0.80
cr_control = 0.10
min_diff = 0.02

cr_var= cr_control + min_diff

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
    z_alpha, z_beta = zScore(sig_lvl, power, tail_input)
    n = ((z_alpha+z_beta)**2) * (((cr_control*(1-cr_control)) + (cr_var*(1-cr_var)))) / (min_diff**2)
    
    return n

def standardErr(cr_control, cr_var, n, tail_input):
    sample_size = sampleSize(sig_lvl, power, cr_control, min_diff, tail_input)
    if tail_input=="one":
        std_err_a = ((cr_control*(1-cr_control))/sample_size)**0.5
        std_err_b = ((cr_var*(1-cr_var))/n)**0.5
    elif tail_input=="two":
        std_err_a = ((cr_control*(1-cr_control))/sample_size)**0.5
        std_err_b = ((cr_var*(1-cr_var))/n)**0.5
    else:
        raise ValueError("Invalid tail value. Choose 'two' for two-tailed test or 'one' for one-tailed test.")
    
    return std_err_a, std_err_b
        
def stdErrDiff(std_err_a, std_err_b):
    std_err_diff = ((std_err_a**2)+(std_err_b**2))**0.5
    return std_err_diff

def re_ZScore(cr_control, cr_var, std_err_a, std_err_b):
    SEDiff = stdErrDiff(std_err_a, std_err_b)
    z_new = (cr_control-cr_var)/(SEDiff)
    
    return z_new
    
def pValue(z_new):
    p_value = 2 * (1 - norm.cdf(abs(z_new)))
    
    return p_value

# cr_var = cr_control + min_diff
n = sampleSize(sig_lvl, power, cr_control, min_diff, tail_input)
std_err_a, std_err_b = standardErr(cr_control, cr_var, n, tail_input)
z_new = re_ZScore(cr_control, cr_var, std_err_a, std_err_b)
finalVal = pValue(z_new)
print("The p-value:", finalVal)

    
    









# p_value = 2 * (1 - norm.cdf(abs(z_score)))

# print("The p-value associated with a z-score of approximately 2.4860 is:", p_value)
