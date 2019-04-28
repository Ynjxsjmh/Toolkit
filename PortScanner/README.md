Python 多线程更建议使用 threading，参考 [廖雪峰 多线程](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832360548a6491f20c62d427287739fcfa5d5be1f000) 以及 [Thread vs. Threading](https://stackoverflow.com/questions/5568555/thread-vs-threading)

这里只是简单实现端口扫描，Python 有个叫做 `python-nmap` 的 package 提供更强大的支持。

如果你想自己构造 TCP 报头玩的话，可以看 [Python 之端口扫描器编写](https://www.cnblogs.com/0xJDchen/p/5954806.html) 做一个引子。因为我也没有刻意去搜这类的，这里不保证该文质量。
