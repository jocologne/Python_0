import time
from datetime import datetime

def main():
	t = time.time()
	date = datetime.fromtimestamp(t)
	print(f"Seconds since January 1, 1970:"
			f"{t: ,.4f} or {t:.2e} in scientific notation")
	print(date.strftime("%b %d %Y"))

if __name__ == "__main__":
	main()