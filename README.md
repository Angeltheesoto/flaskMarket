# flaskMarket

<!--
create a virtual environment [python3 -m venv venv]
activate virtual environment in server with [source venv/scripts/activate]
run server [python3 server.py]
run client [npm start]

NPM PACKAGES
[create-react-app] = frontend web app library.
[axios] =

PIP PACKAGES
[pip install flask] = backend web app framework.
[pip install -U flask-cors] =
 -->

<table class="table table-hover table-dark">
      <thead>
        <tr>
          <!-- Your Columns HERE -->
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Barcode</th>
          <th scope="col">Price</th>
          <th scope="col">Options</th>
        </tr>
      </thead>
      <tbody>
        <!-- Your rows inside the table HERE: -->
        {% for item in items %}
        <tr>
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.barcode }}</td>
          <td>${{ item.price }}</td>
          <td>
            <button class="btn btn-outline btn-info">More Info</button>
            <button class="btn btn-outline btn-success">
              Purchase this item
            </button>
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
