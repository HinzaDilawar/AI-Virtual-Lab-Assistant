import sys
import subprocess
import tempfile
import os
import time

def execute_any_language(language_label, source_code, input_list=None):
    """
    Har language ke programs ko multiple structured inputs ke sath 
    safely run karta hai aur hanging inputs se bachata hai.
    """
    t0 = time.perf_counter()
    tmp_file = None
    suffix_map = {"python": ".py", "cpp": ".cpp", "javascript": ".js"}
    
    # Inputs list ko newline separated string mein convert karein
    if input_list:
        raw_inputs = "\n".join([str(x) for x in input_list]) + "\n"
    else:
        raw_inputs = ""

    # Loop safe-guard: Safe fallback exit commands agar user loop test kar raha ho
    raw_inputs += "\n4\nexit\n0\n"

    try:
        # Create temporary file safely
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix_map[language_label], mode="w", encoding="utf-8") as tf:
            tf.write(source_code)
            tmp_file = tf.name

        # ── Python Execution ──
        if language_label == "python":
            res = subprocess.run(
                [sys.executable, tmp_file],
                input=raw_inputs,
                capture_output=True,
                text=True,
                timeout=5
            )
            if res.returncode == 0:
                return True, res.stdout or "(No output)", time.perf_counter() - t0
            
            err = res.stderr.replace(tmp_file, "script.py")
            if "EOFError" in err:
                return False, "INPUT_NEEDED", time.perf_counter() - t0
            return False, err.strip(), time.perf_counter() - t0

        # ── C++ Execution ──
        elif language_label == "cpp":
            exe_name = tmp_file.replace(".cpp", ".exe" if os.name == "nt" else ".out")
            comp = subprocess.run(["g++", "-std=c++17", tmp_file, "-o", exe_name], capture_output=True, text=True, timeout=15)
            if comp.returncode != 0:
                return False, f"Compilation Error:\n{comp.stderr}", time.perf_counter() - t0
            
            res = subprocess.run([exe_name], input=raw_inputs, capture_output=True, text=True, timeout=5)
            try: os.unlink(exe_name)
            except: pass
            
            if res.returncode == 0:
                return True, res.stdout or "(No output)", time.perf_counter() - t0
            return False, res.stderr.strip() or "INPUT_NEEDED", time.perf_counter() - t0

        # ── JavaScript Execution ──
        elif language_label == "javascript":
            res = subprocess.run(
                ["node", tmp_file],
                input=raw_inputs,
                capture_output=True,
                text=True,
                timeout=5
            )
            if res.returncode == 0:
                return True, res.stdout or "(No output)", time.perf_counter() - t0
            return False, res.stderr.replace(tmp_file, "script.js").strip(), time.perf_counter() - t0

    except subprocess.TimeoutExpired:
        return False, "❌ Time Limit Exceeded (TLE): Infinite loop detect hua hai ya server ne responsive hona band kar diya!", time.perf_counter() - t0
    except Exception as e:
        return False, f"System Error: {str(e)}", time.perf_counter() - t0
    finally:
        if tmp_file and os.path.exists(tmp_file):
            try: os.unlink(tmp_file)
            except: pass