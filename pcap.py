# import os
#
# startdir = '/Users/junaidtariq/Downloads/'
# suffix= '.pcap'
# outputdir = os.path.join(startdir, "Outcsv")
#
# for root, dirs, files, in os.walk(startdir):
#     for name in files:
#         if name.lower().endswith(suffix):
#             sub_folders = root[len(startdir)+1:]
#
#             input_filename = os.path.join(root, name)
#             output_path = os.path.join(outputdir, sub_folders)
#             os.makedirs(output_path, exist_ok=True)  # Ensure the output folder exists
#             output_filename = os.path.join(output_path, os.path.splitext(name)[0] + '.csv')
#
#             cmd = 'tshark -r {} -T fields -e frame.number -e frame.time_relative -e wlan.sa -e wlan.da -e wlan.ta -e wlan.ra -e frame.time_delta_displayed -e frame.len -E header=y -E separator=, -E quote=d -E occurrence=f > {}'
#             final_cmd = cmd.format(input_filename, output_filename)
#
#             print(final_cmd)
#             os.system(final_cmd)


# import socket
# import datetime
# import dpkt
#
#
# def _inet_to_str(inet):
#     try:
#         return socket.inet_ntop(socket.AF_INET, inet)
#     except ValueError:
#         return socket.inet_ntop(socket.AF_INET6, inet)
#
#
# def arp(pcap_path):
#     def _is_arp(packet):
#         return True
#
#     with open(pcap_path, 'rb') as f:
#         pcap = dpkt.pcap.Reader(f)
#         for ts, buf in pcap:
#             eth = dpkt.ethernet.Ethernet(buf)
#             if not isinstance(eth.data, dpkt.ip.IP):
#                 continue
#
#             if not _is_arp(eth):
#                 continue
#             ip = eth.data
#             # write to file instead of printing
#             print('{},{},{}'.format(_inet_to_str(ip.src), _inet_to_str(ip.dst),
#                                     datetime.datetime.utcfromtimestamp(ts).strftime("%m/%d/%Y, %H:%M:%S")))
#
#
# if __name__ == "__main__":
#     arp('/Users/junaidtariq/Downloads/teste.pcap')


import dpkt
file = open('/Users/junaidtariq/Downloads/teste.pcap','rb')
# pcap = dpkt.pcap.Reader(file)
# for ts, buf in pcap:
#     eth = dpkt.ethernet.Ethernet(buf)
#     print(eth)
#
# (ts,buf) = next(pcap)
# eth = dpkt.ethernet.Ethernet(buf)

import pcapkit
# dump to a PLIST file with no frame storage (property frame disabled)
plist = pcapkit.extract(fin='/Users/junaidtariq/Downloads/teste.pcap', fout='out.plist', format='plist', store=False)
# dump to a JSON file with no extension auto-complete
json = pcapkit.extract(fin='/Users/junaidtariq/Downloads/teste.pcap', fout='out.json', format='json', extension=False)
# dump to a folder with each tree-view text file per frame
tree = pcapkit.extract(fin='/Users/junaidtariq/Downloads/teste.pcap', fout='out', format='tree', files=True)