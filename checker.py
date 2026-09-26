#!/usr/bin/env python3
"""
Simple CLI checker for residential solar financing red flags.
For full forensic reviews, visit https://solarpanelscams.com
"""

def evaluate_contract(cash_price, financed_amount, monthly_escalator=False, tax_credit_balloon=False):
    red_flags = []
    dealer_fee = financed_amount - cash_price
    if dealer_fee > 0:
        fee_pct = (dealer_fee / cash_price) * 100
        if fee_pct > 15:
            red_flags.append(f"Excessive Dealer Fee: ${dealer_fee:,.2f} ({fee_pct:.1f}% markup)")
    if monthly_escalator:
        red_flags.append("Predatory Escalator: Monthly rate increases regardless of actual utility rates.")
    if tax_credit_balloon:
        red_flags.append("ITC Re-amortization Trap: Payments jump at Month 18 unless tax credit is prepaid.")
    return red_flags

if __name__ == "__main__":
    print("Solar Contract Red Flag Auditor (https://solarpanelscams.com)")
    flags = evaluate_contract(25000, 35000, True, True)
    for flag in flags:
        print(f" [!] {flag}")
