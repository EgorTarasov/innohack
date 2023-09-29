import { makeAutoObservable, observable, runInAction } from 'mobx';

export class RootStore {
    public trigger: boolean = false;

    constructor() {
        makeAutoObservable(this, {
            trigger: observable,
        });
    }

    public setTrigger() {
        runInAction(() => {
            this.trigger = !this.trigger;
        });
    }
}
