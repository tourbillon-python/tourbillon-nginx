Measurements
************

tourbillon-nginx collects metrics about the server status.

Please refers to  `http://nginx.org/en/docs/http/ngx_http_stub_status_module.html <http://nginx.org/en/docs/http/ngx_http_stub_status_module.html>`_ for more information.


Nginx stats
===========

tourbillon-nginx store metrics in the ``nginx_stats`` series.
Each datapoint is tagged with the Nginx instance hostname and the values collected are:


Tags
----
	* **host**: Nginx instance hostname

Fields
------

    * **connections**: current number of active client connections including waiting connections
    * **total_accepts**: total number of accepted client connections
    * **total_handled**: total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit)
    * **total_requests**: total number of client requests
    * **reading**: current number of connections where nginx is reading the request header
    * **writing**: current number of connections where nginx is writing the response back to the client
    * **waiting**: current number of idle client connections waiting for a request

