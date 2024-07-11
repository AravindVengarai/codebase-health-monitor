from greptile_client import get_codebase_data

def analyze_codebase_health(data):
    health_report = {}
    
    # Analyze average complexity
    try:
        avg_complexity = float(data['average_complexity'])
        if avg_complexity < 5:
            health_report['complexity'] = "Good"
        elif avg_complexity < 10:
            health_report['complexity'] = "Moderate"
        else:
            health_report['complexity'] = "High"
    except Exception as e:
        health_report['complexity'] = "Unable to determine"
    
    # Analyze high complexity functions
    try:
        high_complexity_count = int(data['high_complexity_count'])
        if high_complexity_count == 0:
            health_report['high_complexity'] = "Excellent"
        elif high_complexity_count < 5:
            health_report['high_complexity'] = "Good"
        elif high_complexity_count < 10:
            health_report['high_complexity'] = "Moderate"
        else:
            health_report['high_complexity'] = "Poor"
    except Exception as e:
        health_report['high_complexity'] = "Unable to determine"

    # Analyze outdated dependencies
    try:
        outdated_dependencies = int(data['outdated_dependencies'])
        if outdated_dependencies == 0:
            health_report['outdated_dependencies'] = "Excellent"
        elif outdated_dependencies < 5:
            health_report['outdated_dependencies'] = "Good"
        elif outdated_dependencies < 10:
            health_report['outdated_dependencies'] = "Moderate"
        else:
            health_report['outdated_dependencies'] = "Poor"
    except Exception as e:
        health_report['outdated_dependencies'] = "Unable to determine"

    return health_report

def main():
    print("Retrieving codebase data...")
    codebase_data = get_codebase_data()
    
    print("\nAnalyzing codebase health...")
    health_report = analyze_codebase_health(codebase_data)
    
    print("\nCodebase Health Report:")
    for key, value in health_report.items():
        print(f"{key}: {value}")

    print("\nRaw Data:")
    for key, value in codebase_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
