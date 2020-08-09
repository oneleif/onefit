import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getWorkouts } from "../../actions/workouts";

export class Workouts extends Component {
  render() {
    return (
      <div>
        <h1>Workouts List</h1>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  workouts: state.workouts.workouts,
});

export default connect(Workouts);
