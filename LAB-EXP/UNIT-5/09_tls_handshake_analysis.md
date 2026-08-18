# TLS Handshake Analysis

## TLS handshake overview

1. ClientHello: client sends supported versions, cipher suites, and random values.
2. ServerHello: server picks protocol version, cipher suite, and random values.
3. Certificate: server sends its X.509 certificate to authenticate itself.
4. Key Exchange: keys are negotiated using RSA/ECDHE/DHE.
5. Finished: both sides verify the handshake and start encrypted communication.

## Example packet labels to look for in Wireshark
- ClientHello
- ServerHello
- Certificate
- Server Key Exchange
- Client Key Exchange
- Finished
