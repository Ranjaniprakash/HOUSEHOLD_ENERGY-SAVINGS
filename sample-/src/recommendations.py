def recommend_tips(predicted_usage):
    tips = []
    if predicted_usage > 5.0:
        tips.append("Use LED bulbs to reduce lighting consumption.")
    if predicted_usage > 8.0:
        tips.append("Limit high‑power appliances during peak hours.")
    if predicted_usage > 10.0:
        tips.append("Install a smart thermostat for HVAC control.")
    if not tips:
        tips.append("Great job—your predicted usage is already efficient!")
    return tips
