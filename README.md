# Insecure deserialization vulnerability 

This project presents different data serialization mechanisms and the vulnerabilities arising from performing unchecked
deserialization. This type of vulnerability is potentially extremely severe and it has occurred in the OWASP Top 10
list. The code examples are presenting simple web applications in three different  programming languages with
purposefully built vulnerabilities. 

In the document are presented steps for performing attacks like privilege escalation, remote code execution and denial
of service against the vulnerable applications. For each case solutions for preventing or mitigating the issues are
presented and discussed. 

The main source for the code examples I've used is https://github.com/kojenov/ideabox, so main credit goes to **Alexei
Kojenov**. I've refactored his examples, found a corner case in the Java example, built a sample application for
exploiting it and provided solution for preventing the issue.