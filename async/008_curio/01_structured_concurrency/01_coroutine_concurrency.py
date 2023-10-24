"""
Coroutines can be understood as an alternative concurrency model to shared-state threading (whether system native or not). In the Python community, the threading module is often dismissed as inadequate or even pointless due to the notorious CPython GIL (although there are valid reasons for its existence). GIL aside, however, multithreading as an implementation-agnostic concept is still burdened by a number of issues. In a system with preemptive scheduling and arbitrary concurrent execution, local reasoning becomes significantly more difficult and error prone. Developers must introduce mutex and synchronization mechanisms to protect against race conditions, but the correctness of such mitigations is difficult to verify and must be considered whenever making adjustments to the code or even calling it.

You have to have a level of vigilance bordering on paranoia just to make sure that your conventions around where state can be manipulated and by whom are honoured, because when such an interaction causes a bug it’s nearly impossible to tell where it came from.


"""