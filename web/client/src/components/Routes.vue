<template>
    <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Routes</h1>
        <hr><br><br>

        <div>
          <b-alert variant="success" show>{{ message }}</b-alert>
          <br>
        </div>
        <button type="button"
                class="btn btn-success btn-sm"
                v-b-modal.route-modal>
                Add Route
                </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Location</th>
              <th scope="col">Date</th>
              <th scope="col">Geo</th>
              <th scope="col">Route Name</th>
              <th scope="col">Grade</th>
              <th scope="col">Length</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(route, index) in routes" :key="index">
              <td>{{ route.location }}</td>
              <td>{{ route.date }}</td>
              <td>{{ route.geo }}</td>
              <td>{{ route.routename }}</td>
              <td>{{ route.grade }}</td>
              <td>{{ route.length }}</td>
              <td>
                <div class="btn-group" role="group">
                <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.route-update-modal
                        @click="editRoute(route)">
                        Update
                </button>
                <button type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteRoute(route)">
                          Delete
                </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addRouteModal"
            id="route-modal"
            title="Add a new route"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-location-group"
                    label="Location:"
                    label-for="form-location-input">
          <b-form-input id="form-location-input"
                        type="text"
                        v-model="addRouteForm.location"
                        required
                        placeholder="Enter location">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-date-group"
                      label="Date:"
                      label-for="form-date-input">
            <b-form-input id="form-date-input"
                          type="text"
                          v-model="addRouteForm.date"
                          required
                          placeholder="Enter date">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-geo-group"
                        label="Geo:"
                        label-for="form-geo-input">
              <b-form-input id="form-geo-input"
                            type="text"
                            v-model="addRouteForm.geo"
                            required
                            placeholder="Enter geo">
              </b-form-input>
          </b-form-group>
          <b-form-group id="form-routename-group"
                        label="Route_Name:"
                        label-for="form-routename-input">
              <b-form-input id="form-routename-input"
                            type="text"
                            v-model="addRouteForm.routename"
                            required
                            placeholder="Enter routename">
              </b-form-input>
          </b-form-group>
          <b-form-group id="form-grade-group"
                        label="Grade:"
                        label-for="form-grade-input">
              <b-form-input id="form-grade-input"
                            type="text"
                            v-model="addRouteForm.grade"
                            required
                            placeholder="Enter grade">
              </b-form-input>
          </b-form-group>
          <b-form-group id="form-length-group"
                        label="Length:"
                        label-for="form-length-input">
              <b-form-input id="form-length-input"
                            type="text"
                            v-model="addRouteForm.length"
                            required
                            placeholder="Enter length">
              </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editRouteModal"
         id="route-update-modal"
         title="Update"
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
  <b-form-group id="form-location-edit-group"
                label="Location:"
                label-for="form-location-edit-input">
      <b-form-input id="form-location-edit-input"
                    type="text"
                    v-model="editForm.location"
                    required
                    placeholder="Enter location">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-date-edit-group"
                  label="Date:"
                  label-for="form-date-edit-input">
        <b-form-input id="form-date-edit-input"
                      type="text"
                      v-model="editForm.date"
                      required
                      placeholder="Enter date">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-geo-edit-group"
                    label="Geo:"
                    label-for="form-geo-edit-input">
          <b-form-input id="form-geo-edit-input"
                        type="text"
                        v-model="editForm.geo"
                        required
                        placeholder="Enter geo">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-routename-edit-group"
                      label="Route_Name:"
                      label-for="form-routename-edit-input">
            <b-form-input id="form-routename-edit-input"
                          type="text"
                          v-model="editForm.routename"
                          required
                          placeholder="Enter routename">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-grade-edit-group"
                        label="Grade:"
                        label-for="form-grade-edit-input">
              <b-form-input id="form-grade-edit-input"
                            type="text"
                            v-model="editForm.grade"
                            required
                            placeholder="Enter grade">
              </b-form-input>
            </b-form-group>
            <b-form-group id="form-length-edit-group"
                          label="Length:"
                          label-for="form-length-edit-input">
                <b-form-input id="form-length-edit-input"
                              type="text"
                              v-model="editForm.length"
                              required
                              placeholder="Enter length">
                </b-form-input>
              </b-form-group>

    <b-button-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
    </b-button-group>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      routes: [],
      editForm: {
        id: '',
        location: '',
        date: '',
        geo: '',
        routename: '',
        grade: '',
        length: '',
      },
      addRouteForm: {
        id: '',
        location: '',
        date: '',
        geo: '',
        routename: '',
        grade: '',
        length: '',
      },
      showMessage: true,
    };
  },
  components: {
  },
  methods: {
    getRoutes() {
      const path = 'http://localhost:5000/routes';
      axios.get(path)
        .then((res) => {
          this.routes = res.data.routes;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    updateRoute(payload, routeID) {
      const path = `http://localhost:5000/routes/${routeID}`;
      axios.put(path, payload)
        .then(() => {
          this.getRoutes();
          this.message = 'Route updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRoutes();
        });
    },
    addRoute(payload) {
      const path = 'http://localhost:5000/routes';
      axios.post(path, payload)
        .then(() => {
          this.getRoutes();
          this.message = 'Route added!';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getRoutes();
        });
    },
    initForm() {
      this.addRouteForm.location = '';
      this.addRouteForm.date = '';
      this.addRouteForm.geo = '';
      this.addRouteForm.routename = '';
      this.addRouteForm.grade = '';
      this.addRouteForm.length = '';

      this.editForm.id = '';
      this.editForm.location = '';
      this.editForm.date = '';
      this.editForm.geo = '';
      this.editForm.routename = '';
      this.editForm.grade = '';
      this.editForm.length = '';
    },

    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addRouteModal.hide();
      const payload = {
        location: this.addRouteForm.location,
        date: this.addRouteForm.date,
        geo: this.addRouteForm.geo,
        routename: this.addRouteForm.routename,
        grade: this.addRouteForm.grade,
        length: this.addRouteForm.length,

      };
      this.addRoute(payload);
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRouteModal.hide();
      this.initForm();
      this.getRoutes(); // why?
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addRouteModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRouteModal.hide();
      const payload = {
        location: this.editForm.location,
        date: this.editForm.date,
        geo: this.editForm.geo,
        routename: this.editForm.routename,
        grade: this.editForm.grade,
        length: this.editForm.length,
      };
      this.updateRoute(payload, this.editForm.id);
    },
    editRoute(route) {
      this.editForm = route;
    },
    removeRoute(routeID) {
      const path = `http://localhost:5000/routes/${routeID}`;
      axios.delete(path)
        .then(() => {
          this.getRoutes();
          this.message = 'Route removed!';
          this.showMessage = true;
        })
        .catch((error) => {
        // eslint-disable-next-line
          console.error(error);
          this.getRoutes();
        });
    },
    onDeleteRoute(route) {
      this.removeRoute(route.id);
    },
  },
  created() {
    this.getRoutes();
  },
};
</script>
