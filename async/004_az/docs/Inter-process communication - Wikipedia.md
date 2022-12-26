---
source: https://en.wikipedia.org/wiki/Inter-process_communication \
created: 2022-12-26T15:32:44 (UTC +01:00) \
tags: [] \
author: Contributors to Wikimedia projects
---
# Inter-process communication - Wikipedia
---
For other uses, see [IPC](https://en.wikipedia.org/wiki/IPC_(disambiguation) "IPC (disambiguation)").

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/ArchitectureCloudLinksSameSite.png/260px-ArchitectureCloudLinksSameSite.png)](https://en.wikipedia.org/wiki/File:ArchitectureCloudLinksSameSite.png)

A [grid computing](https://en.wikipedia.org/wiki/Grid_computing "Grid computing") system that connects many personal computers over the Internet via inter-process network communication

In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), **inter-process communication** or **interprocess communication** (**IPC**) refers specifically to the mechanisms an [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") provides to allow the [processes](https://en.wikipedia.org/wiki/Process_(computing) "Process (computing)") to manage shared data. Typically, applications can use IPC, categorized as [clients and servers](https://en.wikipedia.org/wiki/Client%E2%80%93server_model "Client–server model"), where the client requests data and the server responds to client requests.<sup id="cite_ref-microsoft.com_1-0"><a href="https://en.wikipedia.org/wiki/Inter-process_communication#cite_note-microsoft.com-1">[1]</a></sup> Many applications are both clients and servers, as commonly seen in [distributed computing](https://en.wikipedia.org/wiki/Distributed_computing "Distributed computing").

IPC is very important to the design process for [microkernels](https://en.wikipedia.org/wiki/Microkernel "Microkernel") and [nanokernels](https://en.wikipedia.org/wiki/Nanokernel "Nanokernel"), which reduce the number of functionalities provided by the kernel. Those functionalities are then obtained by communicating with servers via IPC, leading to a large increase in communication when compared to a regular monolithic kernel. IPC interfaces generally encompass variable analytic framework structures. These processes ensure compatibility between the multi-vector protocols upon which IPC models rely.<sup id="cite_ref-2"><a href="https://en.wikipedia.org/wiki/Inter-process_communication#cite_note-2">[2]</a></sup>

An IPC mechanism is either [synchronous](https://en.wikipedia.org/wiki/Synchronization_(computer_science) "Synchronization (computer science)") or asynchronous. [Synchronization primitives](https://en.wikipedia.org/wiki/Synchronization_(computer_science)#Implementation_of_Synchronization "Synchronization (computer science)") may be used to have synchronous behavior with an asynchronous IPC mechanism.

## Approaches\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=1 "Edit section: Approaches")\]

Different approaches to IPC have been tailored to different [software requirements](https://en.wikipedia.org/wiki/Software_requirements "Software requirements"), such as [performance](https://en.wikipedia.org/wiki/Algorithmic_efficiency "Algorithmic efficiency"), [modularity](https://en.wikipedia.org/wiki/Software_design "Software design"), and system circumstances such as [network bandwidth](https://en.wikipedia.org/wiki/Bandwidth_(computing) "Bandwidth (computing)") and [latency](https://en.wikipedia.org/wiki/Latency_(engineering) "Latency (engineering)").<sup id="cite_ref-microsoft.com_1-1"><a href="https://en.wikipedia.org/wiki/Inter-process_communication#cite_note-microsoft.com-1">[1]</a></sup>

| Method | Short Description | Provided by ([operating systems](https://en.wikipedia.org/wiki/Operating_system "Operating system") or other environments) |
| --- | --- | --- |
| [File](https://en.wikipedia.org/wiki/Computer_file "Computer file") | A record stored on disk, or a record synthesized on demand by a file server, which can be accessed by multiple processes. | Most operating systems |
| Communications file | A unique form of IPC in the late-1960s that most closely resembles [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs "Plan 9 from Bell Labs")'s [9P protocol](https://en.wikipedia.org/wiki/9P_(protocol) "9P (protocol)") | [Dartmouth Time-Sharing System](https://en.wikipedia.org/wiki/Dartmouth_Time-Sharing_System "Dartmouth Time-Sharing System") |
| [Signal](https://en.wikipedia.org/wiki/Signal_(computing) "Signal (computing)"); also [Asynchronous System Trap](https://en.wikipedia.org/wiki/Asynchronous_System_Trap "Asynchronous System Trap") | A system message sent from one process to another, not usually used to transfer data but instead used to remotely command the partnered process. | Most operating systems |
| [Socket](https://en.wikipedia.org/wiki/Network_socket "Network socket") | Data sent over a network interface, either to a different process on the same computer or to another computer on the network. Stream-oriented ([TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol "Transmission Control Protocol"); data written through a socket requires formatting to preserve message boundaries) or more rarely message-oriented ([UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol "User Datagram Protocol"), [SCTP](https://en.wikipedia.org/wiki/SCTP "SCTP")). | Most operating systems |
| [Unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket "Unix domain socket") | Similar to an internet socket, but all communication occurs within the kernel. Domain sockets use the file system as their address space. Processes reference a domain socket as an [inode](https://en.wikipedia.org/wiki/Inode "Inode"), and multiple processes can communicate with one socket | All POSIX operating systems and Windows 10<sup id="cite_ref-3"><a href="https://en.wikipedia.org/wiki/Inter-process_communication#cite_note-3">[3]</a></sup> |
| [Message queue](https://en.wikipedia.org/wiki/Message_queue "Message queue") | A data stream similar to a socket, but which usually preserves message boundaries. Typically implemented by the operating system, they allow multiple processes to read and write to the [message queue](https://en.wikipedia.org/wiki/Message_queue "Message queue") without being directly connected to each other. | Most operating systems |
| [Anonymous pipe](https://en.wikipedia.org/wiki/Anonymous_pipe "Anonymous pipe") | A unidirectional data channel using [standard input and output](https://en.wikipedia.org/wiki/Stdin "Stdin"). Data written to the write-end of the pipe is buffered by the operating system until it is read from the read-end of the pipe. Two-way communication between processes can be achieved by using two pipes in opposite "directions". | All [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX") systems, Windows |
| [Named pipe](https://en.wikipedia.org/wiki/Named_pipe "Named pipe") | A pipe that is treated like a file. Instead of using standard input and output as with an anonymous pipe, processes write to and read from a named pipe, as if it were a regular file. | All POSIX systems, Windows, AmigaOS 2.0+ |
| [Shared memory](https://en.wikipedia.org/wiki/Shared_memory_(interprocess_communication) "Shared memory (interprocess communication)") | Multiple processes are given access to the same block of [memory](https://en.wikipedia.org/wiki/Memory_(computing) "Memory (computing)"), which creates a shared buffer for the processes to communicate with each other. | All POSIX systems, Windows |
| [Message passing](https://en.wikipedia.org/wiki/Message_passing "Message passing") | Allows multiple programs to communicate using message queues and/or non-OS managed channels. Commonly used in concurrency models. | Used in [LPC](https://en.wikipedia.org/wiki/Local_Inter-Process_Communication "Local Inter-Process Communication"), [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call "Remote procedure call"), [RMI](https://en.wikipedia.org/wiki/Remote_method_invocation "Remote method invocation"), and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface "Message Passing Interface") paradigms, [Java RMI](https://en.wikipedia.org/wiki/Java_RMI "Java RMI"), [CORBA](https://en.wikipedia.org/wiki/CORBA "CORBA"), [COM](https://en.wikipedia.org/wiki/Component_Object_Model "Component Object Model"), [DDS](https://en.wikipedia.org/wiki/Data_Distribution_Service "Data Distribution Service"), [MSMQ](https://en.wikipedia.org/wiki/Microsoft_Message_Queuing "Microsoft Message Queuing"), [MailSlots](https://en.wikipedia.org/wiki/MailSlot "MailSlot"), [QNX](https://en.wikipedia.org/wiki/QNX "QNX"), others |
| [Memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file "Memory-mapped file") | A file mapped to [RAM](https://en.wikipedia.org/wiki/RAM "RAM") and can be modified by changing memory addresses directly instead of outputting to a stream. This shares the same benefits as a standard [file](https://en.wikipedia.org/wiki/File_(computing) "File (computing)"). | All POSIX systems, Windows |

## Applications\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=2 "Edit section: Applications")\]

### Remote procedure call interfaces\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=3 "Edit section: Remote procedure call interfaces")\]

-   [Java](https://en.wikipedia.org/wiki/Java_(programming_language) "Java (programming language)")'s [Remote Method Invocation](https://en.wikipedia.org/wiki/Java_remote_method_invocation "Java remote method invocation") (RMI)
-   [ONC RPC](https://en.wikipedia.org/wiki/ONC_RPC "ONC RPC")
-   [XML-RPC](https://en.wikipedia.org/wiki/XML-RPC "XML-RPC") or [SOAP](https://en.wikipedia.org/wiki/SOAP_(protocol) "SOAP (protocol)")
-   [JSON-RPC](https://en.wikipedia.org/wiki/JSON-RPC "JSON-RPC")
-   Message Bus (Mbus) (specified in RFC 3259) (not to be confused with [M-Bus](https://en.wikipedia.org/wiki/M-Bus_(EN_13757) "M-Bus (EN 13757)"))
-   [.NET Remoting](https://en.wikipedia.org/wiki/.NET_Remoting ".NET Remoting")
-   [gRPC](https://en.wikipedia.org/wiki/GRPC "GRPC")

### Platform communication stack\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=4 "Edit section: Platform communication stack")\]

The following are messaging, and information systems that utilize IPC mechanisms but don't implement IPC themselves:

-   [KDE](https://en.wikipedia.org/wiki/KDE "KDE")'s [Desktop Communications Protocol](https://en.wikipedia.org/wiki/Desktop_communication_protocol "Desktop communication protocol") (DCOP) – deprecated by D-Bus
-   [D-Bus](https://en.wikipedia.org/wiki/D-Bus "D-Bus")
-   [OpenWrt](https://en.wikipedia.org/wiki/OpenWrt "OpenWrt") uses [ubus](https://openwrt.org/docs/techref/ubus) micro bus architecture
-   [MCAPI](https://en.wikipedia.org/wiki/MCAPI "MCAPI") Multicore Communications API
-   [SIMPL](https://en.wikipedia.org/wiki/SIMPL "SIMPL") The Synchronous Interprocess Messaging Project for [Linux](https://en.wikipedia.org/wiki/Linux "Linux") (SIMPL)
-   [9P](https://en.wikipedia.org/wiki/9P_(protocol) "9P (protocol)") (Plan 9 Filesystem Protocol)
-   [Distributed Computing Environment](https://en.wikipedia.org/wiki/Distributed_Computing_Environment "Distributed Computing Environment") (DCE)
-   [Thrift](https://en.wikipedia.org/wiki/Thrift_(protocol) "Thrift (protocol)")
-   [ZeroC](https://en.wikipedia.org/wiki/ZeroC "ZeroC")'s [Internet Communications Engine](https://en.wikipedia.org/wiki/Internet_Communications_Engine "Internet Communications Engine") (ICE)
-   [ØMQ](https://en.wikipedia.org/wiki/%C3%98MQ "ØMQ")
-   [Enduro/X](https://en.wikipedia.org/wiki/Enduro/X "Enduro/X") Middleware
-   [YAMI4](http://www.inspirel.com/yami4)
-   [Enlightenment\_(software)](https://en.wikipedia.org/wiki/Enlightenment_(software) "Enlightenment (software)") E16 uses eesh as an IPC

### Operating system communication stack\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=5 "Edit section: Operating system communication stack")\]

The following are platform or programming language-specific APIs:

-   [Apple Computer](https://en.wikipedia.org/wiki/Apple_Computer "Apple Computer")'s [Apple events](https://en.wikipedia.org/wiki/Apple_events "Apple events"), previously known as Interapplication Communications (IAC)
-   [ARexx](https://en.wikipedia.org/wiki/ARexx "ARexx") ports
-   [Enea's](https://en.wikipedia.org/wiki/ENEA_AB "ENEA AB") [LINX](https://en.wikipedia.org/wiki/LINX_(IPC) "LINX (IPC)") for Linux (open source) and various DSP and general-purpose processors under [OSE](https://en.wikipedia.org/wiki/Operating_System_Embedded "Operating System Embedded")
-   The [Mach kernel](https://en.wikipedia.org/wiki/Mach_kernel "Mach kernel")'s Mach Ports
-   [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft")'s [ActiveX](https://en.wikipedia.org/wiki/ActiveX "ActiveX"), [Component Object Model](https://en.wikipedia.org/wiki/Component_Object_Model "Component Object Model") (COM), [Microsoft Transaction Server](https://en.wikipedia.org/wiki/Microsoft_Transaction_Server "Microsoft Transaction Server") ([COM+](https://en.wikipedia.org/wiki/COM%2B "COM+")), [Distributed Component Object Model](https://en.wikipedia.org/wiki/Distributed_Component_Object_Model "Distributed Component Object Model") (DCOM), [Dynamic Data Exchange](https://en.wikipedia.org/wiki/Dynamic_Data_Exchange "Dynamic Data Exchange") (DDE), [Object Linking and Embedding](https://en.wikipedia.org/wiki/Object_Linking_and_Embedding "Object Linking and Embedding") (OLE), [anonymous pipes](https://en.wikipedia.org/wiki/Anonymous_pipe#Microsoft_Windows "Anonymous pipe"), [named pipes](https://en.wikipedia.org/wiki/Named_pipe#Named_pipes_in_Windows "Named pipe"), [Local Procedure Call](https://en.wikipedia.org/wiki/Local_Procedure_Call "Local Procedure Call"), [MailSlots](https://en.wikipedia.org/wiki/MailSlot "MailSlot"), [Message loop](https://en.wikipedia.org/wiki/Message_loop_in_Microsoft_Windows "Message loop in Microsoft Windows"), [MSRPC](https://en.wikipedia.org/wiki/MSRPC "MSRPC"), [.NET Remoting](https://en.wikipedia.org/wiki/.NET_Remoting ".NET Remoting"), and [Windows Communication Foundation](https://en.wikipedia.org/wiki/Windows_Communication_Foundation "Windows Communication Foundation") (WCF)
-   [Novell](https://en.wikipedia.org/wiki/Novell "Novell")'s [SPX](https://en.wikipedia.org/wiki/IPX/SPX "IPX/SPX")
-   [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX") [mmap](https://en.wikipedia.org/wiki/Mmap "Mmap"), [message queues](https://en.wikipedia.org/wiki/Message_queue "Message queue"), [semaphores](https://en.wikipedia.org/wiki/Semaphore_(programming) "Semaphore (programming)"),<sup id="cite_ref-4"><a href="https://en.wikipedia.org/wiki/Inter-process_communication#cite_note-4">[4]</a></sup> and [shared memory](https://en.wikipedia.org/wiki/Shared_memory_(interprocess_communication) "Shared memory (interprocess communication)")
-   [RISC OS](https://en.wikipedia.org/wiki/RISC_OS "RISC OS")'s messages
-   [Solaris](https://en.wikipedia.org/wiki/Solaris_(operating_system) "Solaris (operating system)") [Doors](https://en.wikipedia.org/wiki/Doors_(computing) "Doors (computing)")
-   [System V](https://en.wikipedia.org/wiki/System_V "System V")'s message queues, semaphores, and shared memory
-   [Linux Transparent Inter Process Communication (TIPC)](https://en.wikipedia.org/wiki/Transparent_Inter-process_Communication "Transparent Inter-process Communication")
-   [OpenBinder](https://en.wikipedia.org/wiki/OpenBinder "OpenBinder") Open binder
-   [QNX](https://en.wikipedia.org/wiki/QNX "QNX")'s PPS (Persistent Publish/Subscribe) service

### Distributed object models\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=6 "Edit section: Distributed object models")\]

The following are platform or programming language specific-APIs that use IPC, but do not themselves implement it:

-   [Libt2n](https://en.wikipedia.org/wiki/Libt2n "Libt2n") for [C++](https://en.wikipedia.org/wiki/C%2B%2B "C++") under Linux only, handles complex objects and exceptions
-   [PHP](https://en.wikipedia.org/wiki/PHP "PHP")'s sessions
-   [Distributed Ruby](https://en.wikipedia.org/wiki/Distributed_Ruby "Distributed Ruby")
-   [Common Object Request Broker Architecture](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture "Common Object Request Broker Architecture") (CORBA)
-   [Electron](https://en.wikipedia.org/wiki/Electron_(software_framework) "Electron (software framework)")'s asynchronous IPC, shares [JSON](https://en.wikipedia.org/wiki/JSON "JSON") objects between a main and a renderer process<sup id="cite_ref-5"><a href="https://en.wikipedia.org/wiki/Inter-process_communication#cite_note-5">[5]</a></sup>

## See also\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=7 "Edit section: See also")\]

-   [Computer network programming](https://en.wikipedia.org/wiki/Computer_network_programming "Computer network programming")
-   [Communicating Sequential Processes](https://en.wikipedia.org/wiki/Communicating_Sequential_Processes "Communicating Sequential Processes") (CSP paradigm)
-   [Data Distribution Service](https://en.wikipedia.org/wiki/Data_Distribution_Service "Data Distribution Service")
-   [Protected procedure call](https://en.wikipedia.org/wiki/Protected_procedure_call "Protected procedure call")

## References\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=8 "Edit section: References")\]

1.  ^ [Jump up to: <sup><i><b>a</b></i></sup>](https://en.wikipedia.org/wiki/Inter-process_communication#cite_ref-microsoft.com_1-0) [<sup><i><b>b</b></i></sup>](https://en.wikipedia.org/wiki/Inter-process_communication#cite_ref-microsoft.com_1-1) ["Interprocess Communications"](http://msdn.microsoft.com/en-us/library/windows/desktop/aa365574(v=vs.85).aspx). Microsoft.
2.  **[^](https://en.wikipedia.org/wiki/Inter-process_communication#cite_ref-2 "Jump up")** Camurati, P (1993). "Inter-process communications for system-level design". _International Workshop on Hardware/Software Codesign_.
3.  **[^](https://en.wikipedia.org/wiki/Inter-process_communication#cite_ref-3 "Jump up")** ["Windows/WSL Interop with AF\_UNIX"](https://blogs.msdn.microsoft.com/commandline/2018/02/07/windowswsl-interop-with-af_unix). Microsoft. 7 February 2018. Retrieved 25 May 2018.
4.  **[^](https://en.wikipedia.org/wiki/Inter-process_communication#cite_ref-4 "Jump up")** "[Concurrent programming - communication between processes](http://www.tldp.org/pub/Linux/docs/ldp-archived/linuxfocus/English/Archives/lf-2003_01-0281.pdf)"
5.  **[^](https://en.wikipedia.org/wiki/Inter-process_communication#cite_ref-5 "Jump up")** ["IpcMain | Electron"](https://www.electronjs.org/docs/api/ipc-main#ipcmain).

-   [Stevens, Richard](https://en.wikipedia.org/wiki/W._Richard_Stevens "W. Richard Stevens"). _UNIX Network Programming, Volume 2, Second Edition: Interprocess Communications._ Prentice Hall, 1999. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [0-13-081081-9](https://en.wikipedia.org/wiki/Special:BookSources/0-13-081081-9 "Special:BookSources/0-13-081081-9")
-   U. Ramachandran, M. Solomon, M. Vernon _[Hardware support for interprocess communication](http://portal.acm.org/citation.cfm?id=30371&coll=portal&dl=ACM)_ Proceedings of the 14th annual international symposium on Computer architecture. Pittsburgh, Pennsylvania, United States. Pages: 178 - 188. Year of Publication: 1987 [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [0-8186-0776-9](https://en.wikipedia.org/wiki/Special:BookSources/0-8186-0776-9 "Special:BookSources/0-8186-0776-9")
-   Crovella, M. Bianchini, R. LeBlanc, T. Markatos, E. Wisniewski, R. _[Using communication-to-computation ratio in parallel program designand performance prediction](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=242738)_ 1–4 December 1992. pp. 238–245 [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier) "ISBN (identifier)") [0-8186-3200-3](https://en.wikipedia.org/wiki/Special:BookSources/0-8186-3200-3 "Special:BookSources/0-8186-3200-3")

## External links\[[edit](https://en.wikipedia.org/w/index.php?title=Inter-process_communication&action=edit&section=9 "Edit section: External links")\]

-   [Linux ipc(5) man page](http://linux.die.net/man/5/ipc) describing System V IPC
-   [Windows IPC](http://msdn.microsoft.com/en-us/library/aa365574(VS.85).aspx)
-   [IPC available using Qt](https://doc.qt.io/qt-5/ipc.html)
-   [Unix Network Programming (Vol 2: Interprocess Communications)](http://www.yendor.com/programming/unix/unp/unp.html) by W. Richard Stevens
-   [Interprocess Communication and Pipes in C](http://technotif.com/basic-guide-interprocess-communication-pipes/)
-   [DIPC, Distributed System V IPC](http://dipc-2.sourceforge.net/)
