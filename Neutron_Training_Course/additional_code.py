import numpy as np 
import matplotlib.pyplot as plt
from pylj import md, util, sample, comp

def nonbond_plots():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlabel('$r_{ij}$/Å')
    ax.set_ylabel('$u$/kJmol$^{-1}$')
    ax.set_xlim([0, 10])
    ax.set_ylim([-10, 10])
    plt.legend()
    plt.tight_layout()
    return fig, ax

def bond_plots():
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].set_xlabel('$b$/Å')
    ax[0].set_ylabel('$u_{bond}$/kJmol$^{-1}$')
    ax[0].set_xlim([1.45, 1.6])
    ax[0].set_ylim([0, 4])
    ax[1].set_xlabel('$θ_{ijk}$/°')
    ax[1].set_ylabel('$u_{angle}$/kJmol$^{-1}$')
    ax[1].set_xlim([112.5, 112.9])
    ax[1].set_ylim([0, 4])
    ax[2].set_xlabel('$ϕ_{ijkl}$/°')
    ax[2].set_ylabel('$u_{dihedral}$/kJmol$^{-1}$')
    ax[2].set_xlim([0, 360])
    ax[2].set_ylim([-1, 1])
    return fig, ax

def velocity_plot():
    fig, ax = plt.subplots(1, figsize=(6, 4))
    ax.set_ylabel('Frequency')
    ax.set_xlabel('v$_i$')
    plt.tight_layout()
    return fig, ax

def periodic_boundary(number_of_steps, temperature):
    """This is a piece of exemplary code to show a single particle traveling across the periodic boundary.

    Parameters
    ----------
    number_of_steps: int
        Number of step in simulation.
    temperature: float
        Temperature of simulation.
    """
    number_of_particles = 1
    sample_freq = 10
    system = md.initialise(number_of_particles, temperature, 50, 'square')
    sampling = sample.JustCell(system)
    system.time = 0
    for i in range(0, number_of_steps):
        system.particles, system.distances, system.forces, system.energies = comp.compute_forces(system.particles, system.box_length, system.cut_off)
        system.particles = md.velocity_verlet(system.particles, system.timestep_length, system.box_length, system.cut_off)
        system = md.sample(system.particles, system.box_length, system.initial_particles, system)
        system.particles = comp.heat_bath(system.particles, system.temperature_sample, temperature)
        system.time += system.timestep_length
        system.step += 1
        if system.step % sample_freq == 0:
            sampling.update(system)
