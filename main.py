from static_analyzer import AnalyzerFunctions, sys, json

def analyze(filepath):
    result = AnalyzerFunctions(filepath)
    
    report = {
        "file_path": filepath,
        "file_type": result.get_file_type(),
        "strings": result.get_strings().split("\n"),
        "libraly_calls": result.get_libraly_calls().split("\n"),
        "system_calls": result.get_system_calls()
    }
    return report

arguments = sys.argv[1:]

if __name__ == "__main__":
    if len(arguments) == 0:
        print("You must input argument")
        sys.exit()
    
    with open("data_results.json", "w", encoding="utf-8") as f:
        json.dump(analyze('/bin/ls'), f, indent=4, ensure_ascii=False)
        