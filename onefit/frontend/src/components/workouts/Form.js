import React, { Component } from "react";
import DateTime from "react-datetime";
import moment from "moment";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addWorkout } from "../../actions/workouts";

export class Form extends Component {
  state = {
    user_name: "",
    date: moment(),
    notes: "",
  };

  static propTypes = {
    addWorkout: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { user_name, date, notes } = this.state;
    const workout = { user_name, date, notes };
    this.props.addWorkout(workout);
  };

  render() {
    const { user_name, date, notes } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Workout</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>user_name</label>
            <input
              className="form-control"
              type="text"
              name="user_name"
              onChange={this.onChange}
              value={user_name}
            />
          </div>
          <div className="form-group">
            <label>Date</label>
            <DateTime
              type="datetime"
              name="date"
              onChange={this.onChange}
              defaultValue={date}
            />
          </div>
          <div className="form-group">
            <label>Notes</label>
            <textarea
              className="form-control"
              type="text"
              name="notes"
              onChange={this.onChange}
              value={notes}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addWorkout })(Form);
