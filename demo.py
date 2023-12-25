from model.micpq import MICPQ
if __name__ == '__main__':
    argparser = MICPQ.get_model_specific_argparser()
    hparams = argparser.parse_args()
    model = MICPQ(hparams)
    model.load()
    print('Loaded model with: %s' % model.flag_hparams())
    val_perf,val_res, test_perf, test_res = model.run_test()
    print(test_res)